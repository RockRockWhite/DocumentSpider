import bs4

from PageSpider.PageSpider import PageSpider


def main():
    res = PageSpider.request_page("https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_1.shtml")
    res2 = PageSpider.deserialize(res, "hello")
    print(res2)


if __name__ == '__main__':
    main()
