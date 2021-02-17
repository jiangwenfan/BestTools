#!/usr/local/python3
#使用ffmpeg,多线程将mp4抽取为mp3
#this is change mp3 from mp4 with ffmpeg
import os
import glob
import threading
import time
#fileList = os.listdir("./")
#print(len(fileList))
#print(fileList)
#for i in fileList:
#	if not os.path.isfile(i):
#		fileList.remove(i)	
#print(len(fileList))
#print(fileList)

mp4List = glob.glob("*.mp4")

def change(mp4file):
	newMp4File = mp4file.replace("：","-") #将原始文件中的中文符号替换为-
	mp3file = "./mp3/"+newMp4File.split(".")[0]+".mp3"
	cmd = "ffmpeg -i "+ mp4file + " -f mp3 -vn " + mp3file
	print(cmd)
	if not os.path.exists("mp3"):
		os.mkdir("mp3")
	print(threading.current_thread())
	os.system(cmd)

def show(n):
	time.sleep(2)
	print("value:"+n)
	print(threading.current_thread())

for mp4File in mp4List:
	#change(mp4File)
	t = threading.Thread(target=change,args=(mp4File,))
	t.start()


#print(len(mp4List))
#print(mp4List)
