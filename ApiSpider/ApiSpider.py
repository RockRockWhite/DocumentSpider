import bs4
import requests

from FileWriter.FileWriter import FileWriter
from PageSpider.PageSpider import PageSpider


class ApiSpider:
    # 验证该url指向的文档时候存在
    @staticmethod
    def url_available(url) -> bool:
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

        return soup.title.text != "公益404"

    @staticmethod
    def get_apis(name, url_format):

        index = 0
        while True:
            index += 1
            url = url_format.format(index=index)

            print(url)

            # 判断接口时候有效
            if not ApiSpider.url_available(url):
                break

            # 获得接口信息
            api = PageSpider.get_api_data(url)

            request_data_page = PageSpider.request_page(url, "请求参数")
            if request_data_page != "":
                data_class = PageSpider.deserialize(request_data_page,
                                                    "{name}_{index}_RequestData".format(name=name, index=index),
                                                    "{api_chinese_name}请求数据".format(
                                                        api_chinese_name=api.chinese_name),
                                                    "详细请参考微信支付官方文档: {url}".format(url=url))
                FileWriter.write_result("./Entities/RequestData/{name}_{index}_RequestData.cs".format(name=name, index=index),
                                        data_class.parse())

            return_json_page = PageSpider.request_page(url, "返回参数")
            if return_json_page != "":
                data_class = PageSpider.deserialize(return_json_page,
                                                    "{name}_{index}_ReturnJson".format(name=name, index=index),
                                                    "{api_chinese_name}返回json".format(
                                                        api_chinese_name=api.chinese_name),
                                                    "详细请参考微信支付官方文档: {url}".format(url=url))
                FileWriter.write_result("./Entities/ReturnJson/{name}_{index}_ReturnJson.cs".format(name=name, index=index),
                                        data_class.parse())


            request_notify_page = PageSpider.request_page(url, "通知参数")
            if request_notify_page != "":
                data_class = PageSpider.deserialize(request_notify_page,
                                                    "{name}_{index}_NotifyJson".format(name=name, index=index),
                                                    "{api_chinese_name}通知参数".format(
                                                        api_chinese_name=api.chinese_name),
                                                    "详细请参考微信支付官方文档: {url}".format(url=url))
                FileWriter.write_result("./Entities/NotifyJson/{name}_{index}_NotifyJson.cs".format(name=name, index=index),
                                        data_class.parse())
        pass
