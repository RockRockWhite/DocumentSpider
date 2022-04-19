import time

import bs4

from ApiSpider.ApiSpider import ApiSpider
from PageSpider.PageSpider import PageSpider


def main():
    for i in range(8, 20):
        for j in range(0, 20):
            time.sleep(2)
            res = ApiSpider.get_apis(f"{i}_Apis",
                                     f"https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter{i}_{j}_{{index}}.shtml")


if __name__ == '__main__':
    main()
