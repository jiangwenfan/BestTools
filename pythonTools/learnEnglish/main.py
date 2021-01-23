#this is a program that helps you remember words.
#根据输入的单词文件(words.csv)输出产生不同单词列表文件。
#generate different lists of words according to different
#chaos(混乱) shun(顺序) fan(倒序)

#encoding:utf-8
import csv
import xlwt
import random


fileName = "words.csv"  #目标原始csv文件
wordsListDict=[]  #总的单词元素[{},{}]
wordsListList = []  # 将所有的单词信息变成列表嵌套列表的，且列表顺序是[key,value]

def create_excel(xlsname,wordsListList):
    """生成excel表格。 传入要生成的文件名,"""
    workbook = xlwt.Workbook(encoding='utf-8') #创建工作簿
    data_sheet = workbook.add_sheet('demo22') #创建sheet
    print("ecel num:"+str(len(wordsListList)))
    for j in range(len(wordsListList)): #j表示总共有多少行
        for i in range(2): #长度为2 0,1,
            data_sheet.write(j , i , wordsListList[j][i],)
    workbook.save(xlsname)

def create_dict(line):
    """将每一行的列表都处理成dict，并添加到总的单词list中."""
    one = {}
    key = line[0]
    value = line[1]
    one[key] = value
    wordsListDict.append(one)

def read_OriginalFile(filename):
    """读取文件将文件中的单词及其汉语变成列表嵌套dict"""
    with open(filename,encoding='utf-8') as f: #指定以utf-8方式打开，因为文件是以utf-8方式保存的。
        content = csv.reader(f)
        num = 0 #统计一共读取了多少行
        for row in content: #读取每一行
            if len(row) != 0:
                create_dict(row) #将每一行都处理成dict并添加
            num += 1
    if len(wordsListDict) == num:
        print("读取成功")
def create_file(mode,type='xls'):
    read_OriginalFile(fileName) #将目标的csv文件读取变成列表。
    if mode == "chaos":
        print("begin to create chaos list.........")
        for i  in range(len(wordsListDict)): #要产生多少次
            dict = random.choice(wordsListDict) #每次随机获取一个列表元素字典
            #xiabiao = wordsListDict.index(suijidict) #获取到这个字典的下标
            temList = []
            for key, value in dict.items(): #获取到每一个en和zh
                if type == 'xls':
                    temList.append(key)  #zh
                    temList.append(value) #en; 将key和value依次添加到字典。
                    wordsListList.append(temList) #将临时列表添加到总的列表中。
                    temList=[] #清空临时小列表
                elif type == 'csv':
                    row_one = key  #zh
                    row_two = value  #en
                    info = row_one + "," + row_two + "\n" #每一行的写入格式。
                    with open('new_chaos.csv', 'a', encoding='utf-8') as f: #没读取一个列表元素，就打开文件写一行，效率不高，后期改进。
                        f.write(info)
                else:
                    print("file type is error!")
            wordsListDict.remove(dict)  # 在原有列表中删除这个dict元素
        print(wordsListList)
        if type == "xls":
            create_excel(xlsname='cahos.xls', wordsListList=wordsListList)
        print("chaos :write ok!................")

    elif mode == "shun":
        print("begin to create shun list.......")
        temList=[] #临时列表
        for dict in wordsListDict:  # dict就是每一个英汉字典{"你好":"hello"}
            for key, value in dict.items(): #获取到每一个en和zh
                if type == 'xls':
                    temList.append(key)  #zh
                    temList.append(value) #en; 将key和value依次添加到字典。
                    wordsListList.append(temList) #将临时列表添加到总的列表中。
                    temList=[] #清空临时小列表
                elif type == 'csv':
                    row_one = key  #zh
                    row_two = value  #en
                    info = row_one + "," + row_two + "\n" #每一行的写入格式。
                    with open('new_shun.csv', 'a', encoding='utf-8') as f: #没读取一个列表元素，就打开文件写一行，效率不高，后期改进。
                        f.write(info)
                else:
                    print("file type is error!")
        if type == "xls":
            create_excel(xlsname='shun.xls', wordsListList=wordsListList)
        print("shun :write ok!................")

    elif mode == "fan":
        print("start to create fan list..........")
        wordsListDict.reverse() #列表反转，返回值为0
        temList = []  # 临时列表
        for dict in wordsListDict: #取出每一个dict{"你好":"hello"}
            for key, value in dict.items():
                if type == 'xls':
                    temList.append(key)  # zh
                    temList.append(value)  # en; 将key和value依次添加到字典。
                    wordsListList.append(temList)  # 将临时列表添加到总的列表中。
                    temList = []  # 清空临时小列表
                elif type == 'csv':
                    row_one = key  # zh
                    row_two = value  # en
                    info = row_one + "," + row_two + "\n"  # 每一行的写入格式。
                    with open('new_fan.csv', 'a', encoding='utf-8') as f:  # 没读取一个列表元素，就打开文件写一行，效率不高，后期改进。
                        f.write(info)
                else:
                    print("file type is error!")
        if type == "xls":
            create_excel(xlsname='fan.xls', wordsListList=wordsListList)
        print("fan : write ok........... ")


    else:
        print("this is error: ",mode)


def main():
    print("this is create words list program")
    print("请事先准备好words.csv这个原始文件.  --> 推荐格式为:[主持人,presenter]这种类型的")
    #file_name = str(input("please input origin file path:"))
    str_mode = str(input("please input words list mode:[chaos,shun,fan]:"+"\n"))
    str_type = str(input("please input view file type: [csv,xls]: ---->默认为xls"+"\n"))
    print(str_type)
    if str_type == "":
        create_file(str_mode)
    else:
        create_file(str_mode,str_type)


if __name__ == '__main__':
    main()
    #print(wordsListDict)

