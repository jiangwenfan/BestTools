#!/usr/local/python3 
#多线程端口扫描器

networkAddress = "192.168.1.0"
networkNetmask = "24"
networkScope = ('1','65535')
#defalut 350 threading scan
#def 

#judge port is or isn't  open , default is 1 to 65535
def portStatus(scope=(1,65535)):
    pass

#show operation info,and how to use
def show():
    print("\n ---- welcome to use port scan tools ----\n")
    global networkAddress
    networkAddress = str(input("please input network address: [eg:192.168.1.0]\n"))
    global networkNetmask
    networkNetmask = str(input("please input network netmask: [eg:24] ----default is 24\n"))
    global networkScope
    networkScope = tuple(input("please input port scope: [eg:1,65535] ----defalut is 1 to 65535\n").split(','))
    
def main():
    show()
    #print(networkAddress) #test
    #print(networkNetmask)
    #print(networkScope)
if __name__ == '__main__':
    main()
