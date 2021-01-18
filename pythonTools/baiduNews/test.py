def test():
    for i in range(30):
        sys.stdout.write('*')
        sys.stdout.flush()  #更新缓冲区
        time.sleep(0.5)
#import math,time

# print(20/3) #除法
# print(20//3) #取整
# print(math.modf(20/3)[0]) #取小数
# print(20%3) #取余数，不是小数
# a = 66
# while a == 66:
#     print("nihao")
#     time.sleep(1)

a = "https://baijiahao.baidu.com/sid=1664814644291885546&wfr=spider&for=pc"

if "?" in a:
    print("ok")

