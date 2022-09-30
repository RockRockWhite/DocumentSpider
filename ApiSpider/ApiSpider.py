# from readline import append_history_file
from pipes import Template
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
    def get_apis(class_name_en, api_name_en, api_name_zh, url):

        have_data = False
        have_return = False

        # api = PageSpider.get_api_data(url)

        ### 请求参数
        request_data_page = PageSpider.request_page(url, "请求参数")
        if request_data_page != "":
            have_data = True
            try:
                data_class = PageSpider.deserialize(request_data_page,
                                                    f"{api_name_en}RequestData",
                                                    f"{api_name_zh}请求数据",
                                                    f"详细请参考微信支付官方文档: {url}")
                FileWriter.write_result(f"./Apis/{class_name_en}/Entities/RequestData/{api_name_en}RequestData.cs",
                                        data_class.parse())
            except:
                have_data =  False

        ### 返回参数
        return_json_page = PageSpider.request_page(url, "返回参数")
        if return_json_page != "":
            have_return = True
            try:
                data_class = PageSpider.deserialize(return_json_page,
                                                    f"{api_name_en}ReturnJson",
                                                    f"{api_name_zh}返回json",
                                                    f"详细请参考微信支付官方文档: {url}")
                FileWriter.write_result(f"./Apis/{class_name_en}/Entities/ReturnJson/{api_name_en}ReturnJson.cs",
                                        data_class.parse())
            except:
                have_return = False


        request_notify_page = PageSpider.request_page(url, "通知参数")
        if request_notify_page != "":
            data_class = PageSpider.deserialize(request_notify_page,
                                                f"{api_name_en}NotifyJson",
                                                f"{api_name_zh}通知参数",
                                                f"详细请参考微信支付官方文档: {url}")
            FileWriter.write_result(f"./Apis/{class_name_en}/Entities/NotifyJson/{api_name_en}NotifyJson.cs",
                                    data_class.parse())
        
        return have_data,have_return
