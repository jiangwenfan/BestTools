import requests
import os
import hashlib
from bs4 import BeautifulSoup
#下载所有校花网的图片到相应的目录中，目录名为当前页的页码
#含有翻页功能

start_url='http://www.xiaohuar.com/hua/'
visited_urls=set()

def md5(url):
    obj=hashlib.md5()
    obj.update(bytes(url,encoding='utf-8'))
    return obj.hexdigest()

def download_img():
    for img  in img_list:
        name=img.attrs.get('alt')
        img_url=img.attrs.get('src')
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        try:
            img_url=img_url.split(":")[1]
            img_url="http:%s"%img_url
        except IndexError:
            img_url="http://www.xiaohuar.com%s"%img_url
        img_response=requests.get(url=img_url)
        def file():
            file_name=name+'.jpg'
            file_path='%s/%s'%(dir_name,file_name)
            #print(file_path)
            with open(file_path,'wb') as f:
                f.write(img_response.content)
        try:
            file()
        except FileNotFoundError:
            print("文件名中含有/错误")
            name=name.split("/")[0] 
            file()


def page(ur=start_url):
    response=requests.get(url=ur)
    response.encoding=response.apparent_encoding
    res_obj=BeautifulSoup(response.text,features='html.parser')
    global img_list
    img_list=res_obj.find(id='list_img').find_all('img')
    a_list=res_obj.find(id='page').find_all('a')
    global dir_name
    dir_name=res_obj.find(id='page').find_all('b')[1].text
    download_img()

    visited_urls.add(md5(start_url))

    for a in a_list:
        page_url=a.attrs.get('href')
        #global page_num
        #page_num=a.text
        if page_url != None:
            md5_page_url=md5(page_url)
            if md5_page_url in visited_urls:
                pass
            else:
                visited_urls.add(md5_page_url)
                #print(page_num,"\n",page_url,"\n") 
                page(page_url)


page()


#def page_num():
#    print(a.split("//")[1].split("/")[1].split("-")[2].split(".")[0])
#
#
#test1
