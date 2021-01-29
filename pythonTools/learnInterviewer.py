#!/usr/local/python3
#create interviewer subject to work!

import csv
import random


import time
print("pleasei prepare file interviewer.csv")
time.sleep(3)

inteviewer = []
with open('interviewer.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row != '': #当读入不为空，才写入。但是似乎不起作用
            inteviewer.append(row)

random.shuffle(inteviewer) #打乱列表

def write(name,value):
    with open(name,'a',encoding='utf-8')  as f:
        f.write(value)
    
for title in inteviewer:
    print(title)
    subject = title[0]
    subject = subject + "\n"
    num = subject[0]
    answer = title[1]
    answer =num + "."+answer + "\n"
    write('subject.txt',subject)
    write('answer.txt',answer)

#print(inteviewer)

