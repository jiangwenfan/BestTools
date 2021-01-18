#获取boss招聘信息
import requests
from bs4 import BeautifulSoup

headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
}
base_url = "https://www.zhipin.com/"
#访问首页，获取所有城市的代码
response = requests.get(url=base_url,headers=headers,verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'html.parser')
#通过ajax请求拿到全部城市，所以不能这样获取到城市代码,后期补充
ul_list = soup.find_all(name='ul',attrs={'class':'city-list'})


#指定城市，获取全部职位
#url = base_url+"shanghai/?ka=city-sites-101020100"
#url = base_url+"job_detail/?query="+"linux%E8%BF%90%E7%BB%B4&"+"city=101020100&industry=&position="
headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
	#'referer':'https://www.zhipin.com/shanghai/?ka=city-sites-101020100',
	'sec-ch-ua':'"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
	'sec-ch-ua-mobile':'?0',
	'sec-fetch-dest':'document',
	'sec-fetch-mode':'navigate',
	'sec-fetch-site':'same-origin',
	'sec-fetch-user':'?1',
	'upgrade-insecure-requests':'1',
'cookie':'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1610937190; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1610937190; __zp_stoken__=ce26bZz1PLUZLPUZicGsMelQ0fxp1ESUXWiBASzAMfzNJNTkeJwl%2FV2IvVFk7XUhlHh8PIE4CcxZHPEkab3NFQCxtWjxlT1hbSUQcBjl1OFskSn9HCWwBPxQkRigVOmxRGE4FGX99IHdsQHV5YQ%3D%3D',
'referer':'https://www.zhipin.com/web/common/security-check.html?seed=uFmbyBX7JBg4luPwEhXz3lzKwz1hU3t48WA41CoAfQQ%3D&name=6bffc4c7&ts=1610937190846&callbackUrl=%2Fjob_detail%2F%3Fquery%3Dlinux%25E8%25BF%2590%25E7%25BB%25B4%26city%3D101020100%26industry%3D%26position%3D&srcReferer='

}
url2 = "https://www.zhipin.com/job_detail/"
data = {
	'query':'linux运维',
	'city':'101020100',
	'industry':'',
	'position':'' 
}
#response = requests.get(url=url2,params=data,headers=headers,verify=False)
response = requests.get(url='https://www.zhipin.com/job_detail/?query=linux%E8%BF%90%E7%BB%B4&city=101020100&industry=&position=',headers=headers,verify=False)
response.encoding = 'utf-8'
#不知道为何还是拿不到职位数据
#通过js加载页面，通过button传入id,通过ajax拿到职位数据
print(response.text)
print(response.status_code)
#print(url2)


