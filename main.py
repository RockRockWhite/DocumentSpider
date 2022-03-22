import bs4

from PageSpider.PageSpider import PageSpider


def main():
    res = PageSpider.request_page("https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_1.shtml", "请求参数")
    res2 = PageSpider.deserialize(res, "hello", "测试类型", "测试注释")
    print(res2.parse())


if __name__ == '__main__':
    main()
