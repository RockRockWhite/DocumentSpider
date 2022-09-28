# from readline import append_history_file
import bs4
import requests
from apis import format_apis

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

        have_data = False
        have_return = False
        if parts[id+1].find("h3") and parts[id+1].find("h3").text=='请求参数':
            have_data = True
        if parts[id+2].find("h3") and parts[id+1].find("h3").text=='返回参数':
            have_return = True
        return req_url,req_method,have_data,have_return

    # 请求页面
    @staticmethod
    def request_page(url, text):
        # url = 'https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter10_3_5.shtml'
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
        if overview == None:
             overview = soup.find("div", clss="overview")

        comment = overview.find_all("p")[1].text
        
        result = []
        all_title = soup.find_all("h2")
        all_part = soup.find_all("div", class_="part")

        if len(all_title)>1:
            pass
        else:
            for id in range(len(all_part)): # 如果有多级h2标题 则需要逐个处理
                h3 = all_part[id].find("h3")
                if h3 is not None and h3.text == text:
                    req_url,req_method,have_data,have_return = RequestSpider.request_para(all_part,id)
                    if req_url==None:
                        continue
                    if req_url.find('http')==-1:
                        print(f'{url.split("/")[-1]}需要手动处理：{req_url}')
                        continue
                    result.append({
                        "comment":comment,
                        "req_url":req_url, 
                        "req_method":req_method, 
                        "have_data":have_data, 
                        "have_return":have_return
                    })
        return result


    @staticmethod
    def get_apis(api_id,api_name):

        url = f'https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/{api_id}.shtml'
        
        res = ''
        try:
            info = RequestSpider.request_page(url, "接口说明")
        except:
            print(f'{url} 出错，需要手动获取')
        else:
            if len(info)==0:
                print(f'{api_id} 需要手动获取')
            else:
                for api_info in info:
                    format_info = format_apis(api_id, api_name, api_info['req_method'], api_info['req_url'], api_info['have_data'], api_info['have_return'])
                    res += f'\n{format_info}'
        return res