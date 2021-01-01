from django.db import models

class UserInfo(models.Model):
    userName = models.CharField(max_length=25) #用户昵称
    userPassword = models.CharField(max_length=25) #用户密码
    userGender = models.CharField(default=0) #默认是男性。0表示男性，1表示女性
    userEmail = models.CharField(max_length=25) #用户电子邮箱
    #userPhoto = models #用户头像
