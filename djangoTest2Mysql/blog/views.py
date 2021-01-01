from django.shortcuts import render,HttpResponseRedirect
from blog.models import BookInfo,HeroInfo
from datetime import date
# Create your views here.

def index(request):
    #b = BookInfo()
    books = BookInfo.objects.all()
    return render(request,'blog/index.html',{'books':books})
def delete(request,bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    return HttpResponseRedirect('/index')
def create(request):
    b = BookInfo()
    b.btitle = '好难'
    b.bpub_date = date(2020,1,1)
    b.save()
    return HttpResponseRedirect('/index')

