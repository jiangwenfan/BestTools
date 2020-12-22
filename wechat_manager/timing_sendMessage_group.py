#encoding:utf-8
import itchat
import time

status = 0
num = 0
group_dict2 = {}
group_dict = {}
itchat.auto_login(hotReload=True)
groupinfo = itchat.get_chatrooms(update=True)
for i in range(len(groupinfo)):
    groupId = groupinfo[i]['UserName'] #获取到群的id
    groupName = groupinfo[i]['NickName'] #获取到群的名字
    group_dict[groupName] = groupId #根据群的名字，存储群的id
    group_dict2[num] = groupName #根据序号，存储群名字
    num += 1 #统计总共有多少个群


print("欢迎使用定时发送群消息的小程序:"+"\n")
print("选择要发送的群的序号:")
for num,name in group_dict2.items():
    print(str(num)+":"+name)
number = int(input("num:"))
message = input("输入你要发送的消息内容:")
target_time = input("选择每天几点钟发送: xx:xx")
target_hour = target_time.split(":")[0]
target_min = target_time.split(":")[1]

groupname = group_dict2[number]
groupid = group_dict[groupname]



current_min = time.localtime().tm_min

while True:
    #month = time.localtime().tm_mon
    #day = time.localtime().tm_mday
    print("2222-------------2")
    current_hour = time.localtime().tm_hour

    if int(target_hour) > current_hour:
        jiange = int(target_hour) - int(current_hour)
        time.sleep(jiange*60*60)

    elif int(target_hour) < current_hour:

        jiange = 24 - int(current_hour)
        jiange = jiange + int(target_hour)
        time.sleep(jiange*60*60)
    else:
        # ==
        print(status)
        if status == 0:
            while True:

                current_min = time.localtime().tm_min
                if int(target_min) == current_min: #判断分钟是否相等
                    itchat.send(message, groupid) #根据group的id发送消息
                    print("第一次发送成功") #打印在终端显示
                    print(status)
                    #global status
                    status = 1
                    break
                time.sleep(10)  # 10秒钟判断一次

            print("正在进行第二次发送")
        else:
            time.sleep(60*65)
##太乱了，有时间整理一下，
##现在可以实现定时发送消息了。


