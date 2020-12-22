#version 1.0
import requests
from bs4 import BeautifulSoup
def SaveImages(name,url,path):
    name = path+name+".jpg"
    print(url)
    image_response = requests.get(url)
    print(image_response)
    with open(name,'wb') as f:
        f.write(image_response.content)

def bing():
    url = "https://bing.ioliu.cn/"
    headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
    page_response = requests.get(url,headers=headers)
    #print(page_response.status_code)
    soup = BeautifulSoup(page_response.text,'html.parser')
    div_list = soup.find_all(name='div',attrs={'class':'container'})
    def diedai(x):
        for i in x:
            img_text = i.find(name='h3').text
            img_name_list  = img_text.split('，')
            if len(img_name_list) > 1:
                img_name = img_name_list[0]
            else:
                img_name_list = img_text.split('(')
                img_name = img_name_list[0]
            img_url = i.find(name='img').get('src') 
            #print(img_text.text)
            SaveImages(img_name,img_url,"/home/jiang/images/")

    count = 0
    for i in div_list:
        count = count + 1
        if count == 2:
            #print(i.text+"\n\n")
            diedai(i)
            count = 0
    #print(div)

bing()

