from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext

# Create your views here.

def index(request):
    temp = loader.get_template('indexContent/index.html')
    content = RequestContext(request,{})
    res_html = temp.render(content)
    return HttpResponse(res_html)

def newest(request):
    temp = loader.get_template('indexContent/newest.html')
    content = RequestContext(request,{})
    res_html = temp.render(content)
    return HttpResponse(res_html)

