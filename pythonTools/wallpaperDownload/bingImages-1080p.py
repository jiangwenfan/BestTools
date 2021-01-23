#version 1.0
import os
import requests
from bs4 import BeautifulSoup

baseUrl = "https://bing.ioliu.cn"
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}
data = {}
path = "./test/" #图片的真是存储路径

#pageResponse = requests.get(url=baseUrl,headers=headers,verify=False)
#pageResponse.encoding = 'utf8'
#print("page status :"+str(pageResponse.status_code))
#soup = BeautifulSoup(pageResponse.text,'html.parser')

"""
传入图片的名字，图片的真实下载地址，真实存储路径
下载图片，存储到指定位置
"""
def saveImages(imageName,imageUrl,realPath):
    imageName = realPath + imageName + ".jpg"
    #print("image url: "+str(imageUrl))
    imageResponse = requests.get(imageUrl,headers=headers,verify=False)
    with open(imageName,'wb') as f:
        f.write(imageResponse.content)

"""
传入页面soup对象，当前所在页面的索引,图片的存储的路径
获取图片名字，和图片的真实下载地址
"""
def getImageInfo(pageSoup,pageIndex,savePath):
    pageIndexName = "page-"+str(pageIndex)
    realPath = savePath + str(pageIndexName) +"/"
    os.mkdir(realPath)
    divList = pageSoup.find_all(name='div',attrs={'class':'container'})[1]
    for divItem in divList:
        imageName = divItem.find(name='div').find(name='div',attrs={'class':'description'}).find(name='h3').text
        imageName = imageName.replace('/','-') #处理文件名中的/
        imageUrl = divItem.find(name='div').find(name='div',attrs={'class':'options'}).find(name='a',attrs={'class':'ctrl download'}).attrs.get('href')
        imageUrl = baseUrl+imageUrl
        saveImages(imageName,imageUrl,realPath)
        print(imageName)
        print(imageUrl)
"""
根据当前页面的soup,传入获取图片的函数。
获取当前页面的索引,判断目标访问深度,根据目标深度进行while递归获取页面的soup，随后传入图片函数
"""
def getIndex():
    soup = getPageSoup(baseUrl,data)
    indexInfo = soup.find(name='div',attrs={'class':'page'}).find(name='span').text 
    currentIndex = indexInfo.split('/')[0].strip()
    sumIndex = indexInfo.split('/')[1].strip()
    if currentIndex < sumIndex:
        nextIndex = int(currentIndex) + 1
        data = {
            'p': nextIndex
        }
        soup = getPageSoup(baseUrl,data)
        #response  = requests.get(url=baseUrl,params=data,headers=headers,verify=False)
        #response.encoding = 'utf-8'
        #soup = BeautifulSoup(response.text,'html.parser')
        getImageInfo(soup,nextIndex,path) #传入获取图片下载地址
        
        
    print(indexInfo)
    print(sumIndex)
    print("--------------------------")
    print(currentIndex)
"""
发送请求，获得页面的soup对象

"""
def getPageSoup(url,data):
    pageResponse = requests.get(url=url,params=data,headers=headers,verify=False)
    pageResponse.encoding = 'utf8'
    print("page status :"+str(pageResponse.status_code))
    soup = BeautifulSoup(pageResponse.text,'html.parser')
    return soup
    
#bing(soup)
getIndex()
#getPageSoup(baseUrl)

