from django.contrib import admin
from simpleShow.models import User,ActivationInfo 

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
class ActivationInfoAdmin(admin.ModelAdmin):
    list_display = ['id','deviceInfo','keyInfo','macInfo','comment']

admin.site.register(User,UserAdmin)
admin.site.register(ActivationInfo,ActivationInfoAdmin)

