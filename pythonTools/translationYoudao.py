#有道翻译

import requests
from bs4 import BeautifulSoup

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {


}
data = {
'i':'翻译',
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':'16109403502235', #加密了
'sign':'756baf9c2ff2c490378acf2012485309',
'lts':'1610940350223',
'bv':'e65e8e5642f3c2d719d32db0b5eff1f9',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTlM'
}
response = requests.post(url=url,headers=headers,data=data)
response.encoding = 'utf-8'
#使用免费的api
print(response.text)
print(response.status_code)
