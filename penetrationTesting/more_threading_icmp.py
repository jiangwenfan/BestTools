import threading
from scapy.all import *
import time

start=time.time()

all=[]
alive=[]
def show_info(args):
    with open('host.txt','a+') as f:
        f.write(args)
def ping(args):
    #name=threading.current_thread().getName()
    for j in args:
        ip='192.168.201.'+str(j)
        package=IP(dst=ip)/ICMP()
        ans,unans=sr(package,timeout=1)
        if list(ans) !=[]:
            host=list(ans)[0][1][IP].src+'\n'
            show_info(host)
        else:
            pass
            #print(" host %s is down "%ip)
    #print(name)
def son_threading():
    for i in range(255):
        all.append(i)
    for j in range(15):
        s1 = 17 * j
        s2 = s1 + 17
        a = 'a' + str(j)
        a = all[s1:s2]
        j = threading.Thread(target=ping, args=(a,))
        #j.setName('a')
        j.start()
t1=threading.Thread(target=son_threading,args=())
t1.start()
t1.join()


    # print("存活的主机：\n")
    # for i in range(len(alive)):
    #     print(alive[i],'\n')
    # name=threading.current_thread().getName()
    # end = time.time()
    # print(end - start)
t2=threading.Thread(target=show_info,args=())
t2.start()
t2.join()
print("main threading!!")








