import requests
from bs4 import BeautifulSoup
##只能下载第一页 img 这是一个低级的测试文件
response=requests.get(url='http://www.xiaohuar.com/hua/')
response.encoding=response.apparent_encoding

res_obj=BeautifulSoup(response.text,features='html.parser')
img_list=res_obj.find(id='list_img').find_all('img')
b=res_obj.find(id='page').find_all('b')
#print(b)
for img  in img_list:
    name=img.attrs.get('alt')
    img_url=img.attrs.get('src')
    #img_url.split(".")
    try:
        img_url=img_url.split(":")[1]
        img_url="http:%s"%img_url
    except IndexError:
        img_url="http://www.xiaohuar.com%s"%img_url

    img_response=requests.get(url=img_url)
    file_name=name+'.jpg'
    with open(file_name,'wb') as f:
        f.write(img_response.content)


    #print(name,"\n",img_url,"\n\n")
