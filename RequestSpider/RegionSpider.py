# from readline import append_history_file
import bs4
import requests


class RegionSpider:

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
    def get_regions(url='https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/index.shtml'):
        if not RegionSpider.url_available(url):
            # print(f'url:{url} 无效')
            return

        headers = {
            "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          r"Chrome/88.0.4324.150 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        }

        # 发送请求
        res = requests.get(url=url, headers=headers)
        res.encoding = "utf-8"

        # 处理请求
        info = {}

        soup = bs4.BeautifulSoup(res.text, "html.parser")
        dl_menu = soup.find("div", class_="doc-menu").find_all("dl")
        for dl in dl_menu:
            title = dl.find("dt").text
            # print("title:",title)
            info[title]={}

            dd_all = dl.find_all("dd")
            for dd in dd_all:
                if dd.find("a") == None:
                    continue
                region = dd.find("a").text
                # print("region:",region)
                info[title][region] = {}
                for chapter in dd.find_all("li"):
                    chapter_id = chapter.get("class")[0]
                    chapter_chinese_name = chapter.find("a").text
                    # print(chapter_id, chapter_chinese_name)
                    info[title][region][chapter_id]=chapter_chinese_name
        
        # print(info)
        return info
        
