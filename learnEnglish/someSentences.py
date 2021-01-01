import os
import random

def createCombination(filePath):
	content=[]
	#judgementFileExist
	if(bool(1-os.path.exists(filePath))):
		print("file not found!")
	else:
		#read file into list type
		with open(filePath,'r') as f:
			for line in f:
				content.append(line.rstrip())
		#get random,get list length
		#num = random.randint(0,len(content))
		#random list
		for i in range(10):
			random.shuffle(content)
			print(content)

createCombination("./test.txt")
	
	 
