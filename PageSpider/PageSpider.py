import re
import bs4
import requests
from bs4.element import Comment

from PageSpider.Api import Api
from PageSpider.DataClass import DataClass
from PageSpider.Property import Property


class PageSpider:

    @staticmethod
    def get_api_data(url):
        api = Api()
        headers = {
            "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          r"Chrome/88.0.4324.150 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        }

        # 发送请求
        res = requests.get(url=url, headers=headers)
        res.encoding = "utf-8"

        # 处理请求
        soup = bs4.BeautifulSoup(res.text, "html.parser")

        api.chinese_name = soup.find("div", class_="overview").h2.text
        api.comment = soup.find("div", class_="overview").find_all("p")[1].text

        # 查找请求参数div_part
        div_part = soup.find_all("div", class_="part")
        for each in div_part:
            if len(each.find_all("p")) < 3:
                api.url = ""
                api.method = ""
                continue

            if each.h3.text == "接口说明":
                if not each.p:
                    api.url = ""
                    api.method = ""
                    continue

                api.url = each.find_all("p")[1].text.replace("请求URL：", "").replace(" ", "")
                api.method = each.find_all("p")[2].text.replace("请求方式：", "").replace(" ", "")

        return api

    # 请求页面
    @staticmethod
    def request_page(url, text):
        headers = {
            "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          r"Chrome/88.0.4324.150 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        }

        # 发送请求
        res = requests.get(url=url, headers=headers)
        res.encoding = "utf-8"

        # 处理请求
        soup = bs4.BeautifulSoup(res.text, "html.parser")

        div_part = soup.find_all("div", class_="part")

        # 查找请求参数div_part
        request_data_tr = None
        for each in div_part:
            if not each.h3:
                continue

            if each.h3.text == text:
                if not each.find("div", class_="table-wrp"):
                    break

                request_data_tr = each.find("div", class_="table-wrp").table.tbody
                break

        if request_data_tr is None:
            return ""

        return request_data_tr

    # 获得首字母以及下划线后字母都大写的类名
    @staticmethod
    def format_class_name(class_name):
        # 首字母大写
        class_name = re.sub(r"^.", class_name[0].upper(), class_name)

        underscore_words = re.findall("_.", class_name)

        for each in underscore_words:
            class_name = class_name.replace(each, each.upper())

        return class_name

    @staticmethod
    # 转换参数名
    def convert_name(name):
        return name.replace(" ", "")

    @staticmethod
    # 转换类型名称
    def convert_type(param_type):

        if re.match("string.*", param_type):
            param_type = "string"

        if re.match("uint64.*", param_type):
            param_type = "ulong"

        if re.match("int64.*", param_type):
            param_type = "long"

        if re.match("uint32.*", param_type):
            param_type = "uint"

        if re.match("int32.*", param_type):
            param_type = "int"

        if re.match("boolean.*", param_type):
            param_type = "bool"

        return param_type

    @staticmethod
    # 转换可为空
    def convert_nullable(text):
        if re.match(r".*是.*", text):
            return True
        else:
            return False

    @staticmethod
    # 转换注释
    def convert_comment(comment):
        return comment.replace("body ", "")

    @staticmethod
    # 转换类型
    def convert_chinese_name(chinese_name):
        # 判断是否为子类型数据
        if re.match(r"\+.*", chinese_name):
            # 除去+
            return chinese_name.replace("+", "").replace(" ", ""), True
        else:
            return chinese_name, False

    @staticmethod
    # 转换array
    def is_array(text):
        if re.match(".*array.*", text):
            return True
        else:
            return False

    @staticmethod
    def deserialize(page_data, name, chinese_name, comment) -> DataClass:
        res = DataClass()
        res.name = name
        res.chinese_name = chinese_name
        res.comment = comment
        res.sub_classes = []
        res.properties = []

        is_sub_class = False
        sub_class_name = ""
        sub_class_chinese_name = ""
        sub_class_comment = ""

        for each in page_data.children:
            if each == "\n":
                continue

            # 排除comment
            if isinstance(each, Comment):
                continue

            # 处理子类型数据
            if is_sub_class:
                is_sub_class = False
                res.sub_classes.append(
                    PageSpider.deserialize(each.find("tbody"), sub_class_name, sub_class_chinese_name,
                                           sub_class_comment))
                continue

            td = each.find_all("td")

            curr_property = Property()
            curr_property.chinese_name, is_sub_class = PageSpider.convert_chinese_name(td[0].text)
            curr_property.name = PageSpider.convert_name(td[1].text)
            curr_property.type = PageSpider.convert_type(td[2].text)
            curr_property.nullable = PageSpider.convert_nullable(td[3].text)

            # 评论需要处理 **多选一** 情况
            if len(td) == 5:
                curr_property.comment = PageSpider.convert_comment(td[4].text)
            else:
                curr_property.comment = PageSpider.convert_comment(td[3].text)
                curr_property.comment += " 多选一"

            if is_sub_class:
                curr_property.type = PageSpider.format_class_name(curr_property.name)
                sub_class_name = curr_property.type
                sub_class_chinese_name = curr_property.chinese_name
                sub_class_comment = curr_property.comment
            # 处理数组
            if PageSpider.is_array(td[2].text.replace(" ", "")):
                if is_sub_class:
                    curr_property.type += "[]"
                else:
                    curr_property.type = "string[]"

            # 将当前参数放入类型
            res.properties.append(curr_property)

        return res
