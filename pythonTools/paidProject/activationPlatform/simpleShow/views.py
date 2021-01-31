from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
import random
import string

# Create your views here.

def index(request):
    return render(request,'key.html')

def showKey(request):
    value = ''.join(random.sample(string.ascii_letters + string.digits, 36))
    softwareType = request.POST.get('softwareType')
    if softwareType == 'software1':
        head = "6B31"
        keyinfo = head + value
        group1 = keyinfo[0:10]
        group2 = keyinfo[10:20]
        group3 = keyinfo[20:30]
        group4 = keyinfo[30:40]
        keyinfo = group1+"-"+group2+"-"+group3+"-"+group4
        print(keyinfo)
        #插入数据库     
        return render(request,'showKey.html',{'keyinfo':keyinfo})
        
    elif softwareType =='software2':
        head = '6B32'
        keyinfo = head + value
        group1 = keyinfo[0:10]
        group2 = keyinfo[10:20]
        group3 = keyinfo[20:30]
        group4 = keyinfo[30:40]
        keyinfo = group1+"-"+group2+"-"+group3+"-"+group4
        print(keyinfo)
        return render(request,'showKey.html',{'keyinfo':keyinfo})
    else:
        print("value is error!")
#def insertSql():
    
