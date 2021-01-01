from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from blog.models import BookInfo,HeroInfo
# Create your views here.

def my_render(request,template_path,contenxt_dict={}):
    temp = loader.get_template(template_path)
    context = RequestContext(request,contenxt_dict)
    res_html = temp.render(context)
    return HttpResponse(res_html)
def index(request):
    #return HttpResponse("舔狗再见!")
    # temp = loader.get_template("blog/index.html")
    # context = RequestContext(resquest,{})
    # res_html = temp.render(context)
    return my_render(resquest,'blog/index.html',{'girl':'hello fat girl','list':list(range(0,10))})

def index2(request):
    return HttpResponse("hello 小胖子!")

def showBooks(request):
    books = BookInfo.objects.all()
    return my_render(request,'blog/showBooks.html',{'books':books})

def details(request,pid):
    book = BookInfo.objects.get(id=pid)
    heros = book.heroinfo_set.all()
    return my_render(request,'blog/details.html',{'book':book,'heros':heros})


