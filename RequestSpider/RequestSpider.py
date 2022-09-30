# from readline import append_history_file
from cgi import print_exception
import bs4
import requests
from ApiSpider.ApiSpider import ApiSpider
from  RequestSpider.apis import format_apis

class RequestSpider:

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
    def request_para(parts, id):
        p_data = parts[id].find_all("p")
        if len(p_data)<3:
            return None,None,None,None
        req_url = p_data[1].text.split('：')[-1]
        req_method = p_data[2].text.split('：')[-1]

        return req_url,req_method

    # 请求某个region下的全部api
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
        overview = soup.find("div", class_="overview")
        if overview == None: # 微信官方的bug
             overview = soup.find("div", clss="overview")

        comment = overview.find_all("p")[1].text
        
        result = []
        all_title = soup.find_all("h2")
        all_part = soup.find_all("div", class_="part")


        for id in range(len(all_part)): # 如果有多级h2标题 则需要逐个处理
            h3 = all_part[id].find("h3")
            if h3 is not None and h3.text == text:
                req_url,req_method = RequestSpider.request_para(all_part,id)
                if req_url==None:
                    continue
                if req_url.find('http')==-1:
                    # print(f'\033[1;31m! ERROR\033[0;0m: {url.split("/")[-1]} 需要手动获取')
                    continue
                result.append({
                    "comment":comment,
                    "req_url":req_url, 
                    "req_method":req_method
                })
        
        
        if len(all_title)>1:
            for index in range(len(result)):
                result[index]['subtitle']=all_title[index+1].text

        return result


    @staticmethod
    def get_apis(api_id, api_name_zh, target_name_en):

        errors = []

        print(f'> 请输入 \033[7;32m{api_name_zh}\033[0;0m 函数名:',end=' ')
        api_name_en = input()

        url = f'https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/{api_id}.shtml'
        
        res = ''
        try:
            info = RequestSpider.request_page(url, "接口说明")
            have_data, have_return = ApiSpider.get_apis(target_name_en, api_name_en, api_name_zh, url)

        except:
            # print_exception()
            print(f'\033[1;31m! ERROR\033[0;0m: {api_id} 需要手动获取')
            errors.append(url)
        else:
            if len(info)==0:
                print(f'\033[1;31m! ERROR\033[0;0m: {api_id} 需要手动获取')
                errors.append(url)
            else:
                for api_info in info:
                    tmp_name = api_name_zh
                    if 'subtitle' in api_info and api_name_zh!=api_info['subtitle']:
                        tmp_name = f'{api_name_zh}:{api_info["subtitle"]}'
                    format_info = format_apis(api_name_en, f"{tmp_name}", api_info['req_method'], api_info['req_url'], have_data, have_return)
                    res += f'\n{format_info}'
        return res, errors