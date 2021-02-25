#!/usr/local/python3
import os
import time

while(True):
    if(os.path.exists('static/info.json')):
        os.system("curl http://sick.pwall.icu:7878/add")
        time.sleep(60)
        os.remove('static/info.json')
    else:
        print("no")
        time.sleep(1)

