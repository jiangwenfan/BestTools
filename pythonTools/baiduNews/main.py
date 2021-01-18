#encoding:utf-8
import os
#问题描述：在天朝上传一些文件或文件夹到云盘(比如，天翼云盘)会检测文件名，如果是文件名包含敏感词，上传进度怎会卡住。

# 获取当前目录下的所有文件和文件名，修改文件名字为:123-->1_my_23
# 进入目录，接着重复上面的步骤。
# 直到全部都是文件，则停止。
# 拓展功能: 生成日志

original_path = 'C:\\Users\\Administrator\\Documents\\Downloads\\'

def get_new_file_name(old_file_name):
    """传入旧的文件名，获取新的文件名"""
    head,*tail = old_file_name #分配变量。head取出首字符，*tail取出剩余字符串. *tail表示很多单个变量，tail表示单个变量组成的列表
    new_tail = "_my_" #新的字符串尾部
    for j in tail:
        new_tail = new_tail + j  #依次取出每个字符，将它拼接到新的字符串尾部
    new_file_name = head + new_tail #整合成新的文件名
    return new_file_name

nameList = os.listdir(path) #获取目标路径下的文件及文件夹名列表
for name in nameList:
    name_path = path +name
    if os.path.isdir(name_path): #判断是目录就进入
        namelist = os.listdir(name_path) #该二层目录下的所有文件及文件夹名列表
        if len(namelist) == 0:
            print("该目录是空的"+name_path)
        else:
            print(namelist)
        #print("this is dir:"+name_path)
    #print(name_path)

def show_dir(path):
    nameList = os.listdir(path) #获取目标路径下的所有文件及文件夹名的列表
    for old_file_name in nameList:   #挨个取出每个文件名及其文件夹名
        old_file_namePath = original_path + old_file_name #每个文件的完整路径
        if os.path.isdir(old_file_namePath): #如果是目录
            #os.rename(a,b) #重命名
            if len(name) != 0:
                #进入目录 show_dir()
        else: #否则如果是文件则进行重命名
            new_file_name = get_new_file_name(old_file_name) #获取新的文件名
            new_file_namePath = path+new_file_name #获取新的文件路径
            os.rename(namepath,new_file_namePath) #重命名

for i in nameList: #每个name都是str
    #每个i表示每个旧的文件名

    filepath = path+i #目标文件的完整路径
    targetpath= path + new_name #改名后的文件路径。如不写会全部移动到当前目录下。
    #os.rename(filepath,new_name) #成功修改第一层文件及其目录名。
print(nameList)