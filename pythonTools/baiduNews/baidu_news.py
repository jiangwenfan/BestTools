import requests
import time
from bs4 import BeautifulSoup

one_url = "https://www.baidu.com/s" #首页url
one_payload={
    "ie":"utf-8",
    "cl":"2",
    "medium":"0",
    "rtt":"1",
    "bsst":"1",
    "rsv_dl":"news_t_sk",
    "tn":"news",
    "word":"阿富汗",
    }
one_headers={
    "Sec-Fetch-Dest":"document",
    "Sec-Fetch-Mode":"navigate",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-User":"?1",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
}

#id_numbers=[] #blank id 列表
dict ={} #每个页面request的参数列表
def send_get(url,dict,headers=one_headers):
    """发送get请求，并将响应体转换为soup对象"""
    response = requests.get(url=url,params=dict,headers=one_headers)
    response.encoding = response.apparent_encoding #自动解码
    body =response.text #获得响应体字符串
    soup = BeautifulSoup(body,'html.parser') #将响应体字符串转为对象
    return soup
def create_payload(url):
    """传入获取到完整url连接，进行分割，替换等等处理生成可以用于发送get请求的payload。"""
    if "?" in url: #判断如果连接中包含?则进行下面操作
        dict.clear()  # 使用字典前先清空
        payload_list = url.split("?")[1].split("&") #?分割获取到url后半段，&分割获取到每个独立的参数列表
        for i in range(len(payload_list)): #根据参数的长度，依次获取到每对参数
            #payload_list[i] 具体的每对参数
            temp = payload_list[i].replace("=",":") #将没对参数中的=替换为:
            a = temp.split(":") #将替换后的每对参数以:进行分割。 a:123 -->a 123
            for i in range(2): #将每对以:号分割后的参数列表进行迭代。
                if i != 1: #仅在i=0时，进行添加到字典。
                    key = a[i]
                    value = a[i+1]
                    dict[key]=value
        #print(dict) #测试添加
        return  dict
def get_page_dict(soup):
    """得到每个翻页的url"""
    p = soup.find(name='p',attrs={'id':"page"})
    for i in range(12):
        a_url=p.find('a').attrs.get('href') #获得每个页码的url
        create_payload(a_url)
def get_news_dict(soup):
    """得到每个具体新闻的url"""
    for i in range(11):
        if i != 0:
            div = soup.find(name='div', attrs={'id': i})  # 结果是对象
            a = div.find('h3').find("a")
            page_url = a.attrs.get("href")
            # with open("url.txt", 'a') as f: #最后成功之后会删掉，是一个中间产物
            #     f.write(page_ulr)
            #     f.write("\n")
            return create_payload(page_url)

            # res = requests.get(page_ulr, params=dict)
            # res.encoding = "utf-8"
def get_all_news(soup):
    news_dict = get_news_dict(soup)
    soup = send_get(url=one_url,dict=news_dict) #发送具体news请求，返回页面的soup对象
    print(soup.text) #显示新闻文本
def page_depth(num,soup):
    for i in range(int(num)):
        page_dict = get_page_dict(soup)
        soup = send_get(url=one_url,dict=page_dict) #发送翻页请求，返回页面的soup对象
        get_all_news(soup)


soup = send_get(url=one_url, dict=one_payload,headers=one_headers)
page_depth(18,soup)










