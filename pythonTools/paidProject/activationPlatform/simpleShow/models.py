from django.db import models

# Create your models here.

class User(models.Model):
    """administrator"""
    def __str__(self):
        return self.username
    username = models.CharField(max_length=20)
    userpassword = models.CharField(max_length=30)

class ActivationInfo(models.Model):
    """activation info"""
    def __str__(self):
        return self.deviceInfo
    cpuInfo = models.CharField(max_length=50)
    macInfo = models.CharField(max_length=50)
    memoryInfo = models.CharField(max_length=100)
    gpuInfo = models.CharField(max_length=100)
    keyInfo = models.CharField(max_length=200)
    deviceInfo = models.CharField(max_length=30) #自行备注
    comment = models.CharField(max_length=30)

    
