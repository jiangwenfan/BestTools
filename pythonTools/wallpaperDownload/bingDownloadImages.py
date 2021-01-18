#version 1.0
import requests
from bs4 import BeautifulSoup

baseUrl = "https://bing.ioliu.cn"
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}
#path = "/home/jiang/aa/" #图片的真是存储路径

def saveImages(imageName,imageUrl,saveImagePath):
    imageName = saveImagePath+imageName+".jpg"
    #print("image url: "+str(imageUrl))
    imageResponse = requests.get(imageUrl,headers=headers,verify=False)
    with open(imageName,'wb') as f:
        f.write(imageResponse.content)

def bing():
    pageResponse = requests.get(url=baseUrl,headers=headers,verify=False)
    pageResponse.encoding = 'utf8'
    print("page status :"+str(pageResponse.status_code))
    soup = BeautifulSoup(pageResponse.text,'html.parser')
    divList = soup.find_all(name='div',attrs={'class':'container'})[1]
    for divItem in divList:
        imageName = divItem.find(name='div').find(name='div',attrs={'class':'description'}).find(name='h3').text
        imageName = imageName.replace('/','-') #处理文件名中的/
        imageUrl = divItem.find(name='div').find(name='div',attrs={'class':'options'}).find(name='a',attrs={'class':'ctrl download'}).attrs.get('href')
        imageUrl = baseUrl+imageUrl
        saveImages(imageName,imageUrl,"./test/")
        print(imageName)
        print(imageUrl)
    
    print("--------------------------")
    #def diedai(x):
    #    for i in x:
    #        img_text = i.find(name='h3').text
    #        img_name_list  = img_text.split('，')
    #        if len(img_name_list) > 1:
    #            img_name = img_name_list[0]
    #        else:
    #            img_name_list = img_text.split('(')
    #            img_name = img_name_list[0]
    #        img_url = i.find(name='img').get('src') 
    #        #print(img_text.text)
    #        SaveImages(img_name,img_url,"/home/jiang/")

    #count = 0
    #for i in div_list:
    #    count = count + 1
    #    if count == 2:
    #        #print(i.text+"\n\n")
    #        diedai(i)
    #        count = 0
    ##print(div)

bing()

