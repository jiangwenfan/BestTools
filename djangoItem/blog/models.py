from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    def __str__(self):
        #返回书名
        return self.btitle

#一个本书中含有多个英雄，一对多。
#英雄类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20) #名字
    hgender = models.BooleanField(default=False) #性别。
    hcomment = models.CharField(max_length=128)
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname
    #