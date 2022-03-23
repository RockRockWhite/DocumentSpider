import bs4

from ApiSpider.ApiSpider import ApiSpider
from PageSpider.PageSpider import PageSpider


def main():
    # res = ApiSpider.url_available("https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_13.shtml")
    # print(res)
    # res = PageSpider.request_page("https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_13.shtml", "请求参数")
    # if res != "":
    #     res2 = PageSpider.deserialize(res, "hello", "测试类型", "测试注释")

    # res3 = PageSpider.request_page("https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_1.shtml", "通知参数")
    # if res3 != "":
    #     res4 = PageSpider.deserialize(res3, "hello", "测试类型", "测试注释")
    #     print(res4.parse())
    #
    # api = PageSpider.get_api_data("https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_1.shtml")
    # print(api)
    # ApiSpider.url_available("https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_2.shtml")

    res = ApiSpider.get_apis("test_api",
                             "https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_{index}.shtml")


if __name__ == '__main__':
    main()
