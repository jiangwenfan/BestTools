#encoding:utf-8

#this is a program of show a progress bar.

import os
import sys,time,threading


def get_size(file,file2,interval_time=1.5):
    """file时原始文件的路径;file2时目标文件的路径"""
    status = [0]
    while status[0] == 0:
        origin_file_size = int(os.path.getsize(file))/1024/1024  #得到原始文件的大小,MB
        current_file_size = int(os.path.getsize(file2))/1024/1024    #当前文件大小，MB

        print(type(origin_file_size))
        number_list = str(current_file_size / origin_file_size).split(".") #将当前文件大小和原始文件大小做比值，拿到整数和小数列表
        num_one = number_list[0]  # 取整数
        num_two = number_list[1]  # 取小数
        num1, num2, num3, *null = num_two  # 小数第一位和小数第二位,*null去掉其他数字位数

        if num_one != 1:
            print("\n" + "---------当前进度-------------------")
            for one in range(int(num1)):
                "打印次数最慢的"
                sys.stdout.write("#")
                time.sleep(0.15)
                #status[0] =0
            print("\r")
            for two in range(int(num2)):
                sys.stdout.write("#")
                time.sleep(0.15)
            print("\r")
            for three in range(int(num3)):
                sys.stdout.write("#")
                time.sleep(0.15)
        else:
            print("操作完成!")
            status[0]=1


get_size("F:\\cell.csv","‪F:\\doc\\git\\docker.pdf")
