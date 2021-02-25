from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from simpleShow.models import ActivationInfo
import json
import random
import string

# Create your views here.

def index(request):
    return render(request,'key.html')

def showKey(request):
    softwareType = request.POST.get('softwareType')
    time = int(float(request.POST.get('time')))
    if softwareType == 'software1':
        head = "6B31"
        keyinfoList = []
        while(time):    
            value = ''.join(random.sample(string.ascii_letters + string.digits, 36))
            keyinfo = head + value
            group1 = keyinfo[0:10]
            group2 = keyinfo[10:20]
            group3 = keyinfo[20:30]
            group4 = keyinfo[30:40]
            keyinfo = group1+"-"+group2+"-"+group3+"-"+group4
            keyinfoList.append(keyinfo)
            time = time -1
            print(keyinfo)
        return render(request,'showKey.html',{'keyinfoList':keyinfoList})
        
    elif softwareType =='software2':
        head = '6B32'
        keyinfoList = []
        while(time):    
            value = ''.join(random.sample(string.ascii_letters + string.digits, 36))
            keyinfo = head + value
            group1 = keyinfo[0:10]
            group2 = keyinfo[10:20]
            group3 = keyinfo[20:30]
            group4 = keyinfo[30:40]
            keyinfo = group1+"-"+group2+"-"+group3+"-"+group4
            keyinfoList.append(keyinfo)
            time = time -1
            print(keyinfo)
        return render(request,'showKey.html',{'keyinfoList':keyinfoList})
    else:
        print("value is error!")
def add(request):
    with open('static/info.json','r') as f:
        infoList = json.load(f) 
    #select
    currentKey = infoList[0]['keyInfo']
    ais = ActivationInfo.objects.filter(keyInfo=currentKey)
    if len(ais) == 0:
        print("add")
        #add
        ai = ActivationInfo() 
        ai.cpuInfo = infoList[0]['cpuInfo']
        ai.memoryInfo = infoList[0]['memoryInfo']
        ai.gpuInfo = infoList[0]['gpuInfo']
        ai.macInfo = infoList[0]['macInfo']
        ai.keyInfo = infoList[0]['keyInfo']
        ai.deviceInfo = infoList[0]['deviceInfo'] 
        ai.comment = infoList[0]['comment']
        ai.save()
        data = {"status":"success"}
        with open('static/data.json','w') as f:
            json.dump(data,f)
        return HttpResponse("add register ok")
    elif len(ais) == 1:
        #exists
        sqlcpuInfo = ais[0].cpuInfo
        sqlmemoryInfo = ais[0].memoryInfo
        sqlgpuInfo = ais[0].gpuInfo
        sqlmacInfo = ais[0].macInfo
        #get json info
        jsoncpuInfo = infoList[0]['cpuInfo']
        jsonmemoryInfo = infoList[0]['memoryInfo']
        jsongpuInfo = infoList[0]['gpuInfo']
        jsonmacInfo = infoList[0]['macInfo']
        if sqlcpuInfo == jsoncpuInfo and sqlmemoryInfo == jsonmemoryInfo and sqlgpuInfo == jsongpuInfo and sqlmacInfo == jsonmacInfo:
            data = {"status":"success"}
            with open('static/data.json','w') as f:
                json.dump(data,f)
            return HttpResponse("register ok")
        else:
            data = {"status":"fail"}
            with open('static/data.json','w') as f:
                json.dump(data,f)
            return HttpResponse("repetition")
        print(sqlcpuInfo)
        print(jsoncpuInfo)
    else:
        print("error")
    
