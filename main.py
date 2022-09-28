import time
import bs4
from ApiSpider.ApiSpider import ApiSpider
from PageSpider.PageSpider import PageSpider

def main():
    print('hello')
    for i in range(4, 10):
        for j in range(1, 20):
            print(i,j)
            time.sleep(2)
            res = ApiSpider.get_apis(f"{i}_Apis",
                                     f"https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter{i}_{j}_{{index}}.shtml")
            print(res)


if __name__ == '__main__':
    main()
