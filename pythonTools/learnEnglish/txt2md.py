#!/usr/local/python3
#把目标txt文本的单词转为md格式显示
import os

path = "newtest2.txt" #要读取的文件
targetFile = "new2.md" #要输出的文件
count = 5 #几个单词一组

try:
    os.remove(targetFile)
except FileNotFoundError as e:
    print("file not exists,skip delting."+str(e))

def writeMd(content):
    with open(targetFile,'a') as f:
        f.write(content)
def change(path):
    with open(path,'r') as f:
        times = 0 #0
        for i in f:
            i = i.rstrip("\n")
            i = "**"+i+"**"+"\n"
            if times == count:
                writeMd("***"+"\n")
                writeMd(i)
                times = 0
            else:
                writeMd(i)
                times += 1

if __name__ == "__main__":
    change(path)
