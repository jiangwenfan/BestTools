#version 1.0
import os
import random

img_num = 0 
img_path_list = []

#duration1 = "30"    #壁纸默认持续时间
#img1_path = "a/b/test.png"
#img2_path = "a/b/test2.jpg"

#wallpaperConfigFile = "none"    #随机生成的自定义壁纸配置文件

info_head = '''
<background>
    
    <starttime>
        <year>2020</year>
        <month>3</month>
        <day>07</day>
        <hour>00</hour>
        <minute>00</minute>
        <second>00</second>
    </starttime>
'''
info_tail = "</background>"

def xml1_middle(duration1,img1_path,img2_path):
    info_middle = '''
        <static>
            <duration>'''+duration1+'''</duration>
            <file>'''+img1_path+'''</file>
        </static>
        <transition>
            <duration>'''+"1"+'''</duration>
            <from>'''+img1_path+'''</from>
            <to>'''+img2_path+'''</to>
        </transition>
    '''
    return info_middle

info2_head = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
<wallpapers>

"""
def xml2_middle(wallpaperConfigFile):
    info2_middle = """
    <wallpaper deleted="false">
        <name>mypybackground</name>
        <filename>"""+wallpaperConfigFile+"""</filename>
        <options>zoom</options>
    </wallpaper>
    """
    return info2_middle
info2_tail = """
</wallpapers>
"""

def randomNumber(bit):
    """create random wallpaper config file  name"""
    randomFileName = "py";
    for i in range(bit):
        num = random.randint(0,9)
        randomFileName = randomFileName+str(num)
    return randomFileName;

def get_imgPath(): #
    """get each image path"""
    path = "/home/jiang/images/"  #将来传入实际目录
    global img_num
    img_num = int(os.popen("ls -l "+path+" | wc -l").read()) - 1
    for i in range(img_num):
        img_name = os.listdir(path)[i]
        img_path = path+img_name
        img_path_list.append(img_path)

def modifyFile1(xmlName1,duration):
    """modification  first wallpaper xml config file"""
    get_imgPath() #得到图片实际路径列表

    with open(xmlName1,'a') as f:
        f.write(info_head)   #写入xml文件头
        for i in range(img_num):
            img1_path = img_path_list[i]
            if i+2 >= len(img_path_list):
                img2_path = img_path_list[0]
            else:
                img2_path = img_path_list[i+1]

            f.write(xml1_middle(duration, img1_path, img2_path))
        f.write(info_tail)

def modifyFile2(xmlName2,wallpaper_config_file):
    """modification second systemctl xml config file"""
    os.system("echo \" \"  >"+xmlName2)  #清空配置文件
    with open(xmlName2,'a') as f:
        f.write(info2_head)
        f.write(xml2_middle(wallpaper_config_file))
        f.write(info2_tail)

def main():
    """main 文件"""
    str = os.popen("lsb_release -a | grep Codename").read()
    Codename = str.split()[1]    #读取系统版本及
    base = "/usr/share/backgrounds/contest/"
    backup_file = base+Codename+ "_py3_backup" + ".xml" #生成xml１的备份文件名
    os.system("cp "+base+Codename+".xml"+"  "+backup_file ) #备份xml1文件

    base2 = "/usr/share/gnome-background-properties/"
    xmlFile2 =  base2+Codename+"-wallpapers.xml"
    os.system("cp  "+xmlFile2+"  "+base2+Codename+"-wallpapers_py3_backup.xml") #备份xml文件
    
    fileName１ = base+randomNumber(4)+".xml"
    os.system("touch "+fileName１)   #create new wallpapers xml file
    modifyFile1(fileName１,"60")

    modifyFile2(xmlFile2,fileName１)


if __name__ == "__main__":
    main()

