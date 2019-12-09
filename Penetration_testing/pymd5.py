#!/usr/bin/python3
import hashlib
print("输入flag值进行hash运算，生成字符串")
str=input("please input flag string:")
obj=hashlib.md5()
obj.update(str.encode('utf-8'))
print("\n")
print(obj.hexdigest())
print("\n")
