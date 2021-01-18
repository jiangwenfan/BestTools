#get the weather
import requests
from bs4 import BeautifulSoup

url="http://www.weather.com.cn/"
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

city_info = [] #存储所有城市信息
international_city_info = {} #国际
mainland_city_info = {}

#发送请求
response = requests.get(url=url,headers=headers)
response.encoding='utf-8'
#test
print(response.status_code)

#获取热门城市列表
soup = BeautifulSoup(response.text,'html.parser')
#国内的
div = soup.find(name='div',attrs={'class':'w_city city_guonei'})
dl = div.find_all(name='dl')[0]
dd = dl.find(name='dd')
a_city_list = dd.find_all(name='a')
for a_city in a_city_list:
	city_name = a_city.attrs.get('title')
	city_url = a_city.attrs.get('href')
	if city_name in mainland_city_info:
		print("key is exists"+city_name)
	else:
		mainland_city_info[city_name] = city_url
#test
#print(mainland_city_info)
#国际的
dd_all_list = soup.find_all(name='dd',attrs={'class':'jind'})
dd_city_list = dd_all_list[-1]
a_city_list = dd_city_list.find_all(name='a')
for a_city in a_city_list:
	city_name = a_city.attrs.get('title')
	city_url = a_city.attrs.get('href')
	if city_name in international_city_info:
		print("key is exists!"+city_name)
	else:
		international_city_info[city_name] = city_url
#test
#print(international_city_info)

#获取当天气温
#获取国内
def get_weather(url):
	response = requests.get(url=url,headers=headers)
	response.encoding = 'utf-8'
	#print(url)
	print(response.status_code)
	soup = BeautifulSoup(response.text,'html.parser')
	div = soup.find(name='div',attrs={'id':'today'}).find(name='div',attrs={'class':'t'})
	li_list = div.find(name='ul').children 
	li_list_new = []
	for ele in li_list: #去掉换行符，生成新的列表
		if ele != '\n':
			li_list_new.append(ele)
	daytime_li = li_list_new[0]
	night_li = li_list_new[1] 
	
	daytime_info = {} #白天天气信息
	night_info = {} #晚上天气信息
	
	#获取白天天气信息,存储
	time = daytime_li.find(name='h1').text #17日白天
	#weather_image =  天气图片
	weather_text = daytime_li.find(name='p',attrs={'class':'wea'}).attrs.get('title') #晴
	temperature = daytime_li.find(name='p',attrs={'class':'tem'}).find(name='span').text #5 5摄氏度
	wind1 = daytime_li.find(name='p',attrs={'class':'win'}).find(name='span').attrs.get('title') #北风
	wind2 = daytime_li.find(name='p',attrs={'class':'win'}).find(name='span').text #3-4级
	wind = str(wind1)+str(wind2)
	sunrise = daytime_li.find(name='p',attrs={'class':'sun sunUp'}).find(name='span').text #日出 6:52  
	daytime_info['time'] = time
	daytime_info['weather_text'] = weather_text
	daytime_info['temperature'] = temperature
	daytime_info['wind'] = wind
	daytime_info['sunrise'] = sunrise
	
	#获取晚上天气信息存储
	time = night_li.find(name='h1').text #17日晚上
	weather_text = night_li.find(name='p',attrs={'class':'wea'}).attrs.get('title')
	temperature = night_li.find(name='p',attrs={'class':'tem'}).find(name='span').text
	wind1 = night_li.find(name='p',attrs={'class':'win'}).find(name='span').attrs.get('title')
	wind2 = night_li.find(name='p',attrs={'class':'win'}).find(name='span').text 
	wind  = wind1 + wind2
	sunset = night_li.find(name='p',attrs={'class':'sun sunDown'}).find(name='span').text
	night_info['time'] = time
	night_info['weather_text'] = weather_text
	night_info['temperature'] = temperature
	night_info['wind'] = wind
	night_info['sunset'] = sunset
	
	print(daytime_info)
	print(night_info)

#test
url = mainland_city_info['上海']
get_weather(url)
#test
#for key in mainland_city_info.keys():
#	url = mainland_city_info[key] 
#	print("当前城市是:"+str(key))
#	get_weather(url)

#获取国际城市
#test 国际成熟需要重新匹配
for key in international_city_info.keys():
	url = international_city_info[key]
	print("当前城市是:"+str(key))
	get_weather(url)

