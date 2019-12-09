#!/usr/bin/python3

#多线程icmp扫描，可以用，但是一个半成品。
#
import threading
from scapy.all import *

network_num=str(input("输入网段[eg:192.168.201.] : "))
all_ip=[]

for i in range(255):
    ip=network_num+str(i)
    all_ip.append(ip)

def scan(args):
    for i in args:
        package=IP(dst=i)/ICMP()
        ans,unans=sr(package,timeout=1)
        if list(ans) !=[]:
            alive_ip=list(ans)[0][1][IP].src+'\n'
            with open('host_alive.txt','a+') as f:
                f.write(alive_ip)
        else:
            pass

def son_threading():
    for j in range(15):
        start_num=17*j
        end_num=start_num+17
        ip_range=all_ip[start_num:end_num]
        j=threading.Thread(target=scan,args=(ip_range,))
        j.start()

if __name__=='__main__':
    son_threading()
    #print(all_ip[17:34])
    #scan(all_ip[17:34])

