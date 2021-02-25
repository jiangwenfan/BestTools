#!/usr/local/python3
#根据需要筛选出指定长度的单词
import os


path = "./CET4.txt" #原始文件. 根据要求修改
length = 4 #希望要找出单词的长度
scope = "<=" #希望要找出单词长度的条件
targetFile = "newtest2.txt" #输出的新文件


#clear target file
try:
    os.remove(targetFile)
except FileNotFoundError as e:
    print("The target file does not exists,skip deleting "+str(e))

# write content to new file
def writeTxt(content):
    with open(targetFile,'a') as f:
        f.write(content)

#read file 
def readTxt(path):
    with open(path,'r') as f:
        for i in f:
            i = i.rstrip("\n") #remove every line "\n"
            if len(i) > 0:  #remove blank line
                if len(i) > 1: #remove single letter
                    wordInfo = i.split(" ")
                    word = wordInfo[0]
                    if scope == "<=" or scope == "=<":
                        if len(word) <= length:
                            writeTxt(i+"\n")
                        else:
                            #writeTxt("no"+str(len(word))+"\n")
                            pass
                    if scope == "==" or scope == "=":
                        if len(word) == length:
                            writeTxt(i+"\n")
                    if scope == ">=" or scope == "=>":
                        if len(word) >= length:
                            writeTxt(i+"\n")
                else:
                    #print("single letter:- "+i)
                    pass
            else:
                #print("blank line---:"+str(len(i)))
                pass

    
if __name__ == '__main__':
    readTxt(path)
