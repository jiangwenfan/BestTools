#!/usr/bin/python3

#多线程icmp扫描进阶，但也是一个半成品。

import threading
from scapy.all import *

network_num=input("输入网段【eg:192.168.201.】:")
all_ip=[]

for i in range(255):
		#生成所有IP，存在列表中
		ip=network_num+i
		all_ip.append(ip)

def scan(args):
	#imcp 扫描特定ip，处理扫描结果。
	for i in args:
		package=IP(dst=ils)/ICMP()
		ans,unans=sr(package,timeout=1)
        if list(ans) !=[]:
            alive_ip=list(ans)[0][1][IP].src+'\n'
            with open('host_alive.txt','a+') as f:
				f.write(alive_ip)
        else:
            pass
	
def son_threading():
	#15个子线程开始启动
	for j in range(15):
		start_num=17*j  #每个线程要扫描的开始ip的下标
		end_num=start_num+17 #结束下标。
		ip_range=all_ip[start_num,end_num] #每个线程要扫描的ip范围
		#threading_name='a'+str(j) #每个子线程名a1
		j=threading.Thread(target=scan,args=(ip_range,))
		j.start()

if __name__='__main__':
	son_threading()
		
		
		
		
			
	
		