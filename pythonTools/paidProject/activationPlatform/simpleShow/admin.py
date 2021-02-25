from django.contrib import admin
from simpleShow.models import User,ActivationInfo 

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
class ActivationInfoAdmin(admin.ModelAdmin):
    list_display = ['id','deviceInfo','keyInfo','macInfo','comment']

admin.site.register(User,UserAdmin)
admin.site.register(ActivationInfo,ActivationInfoAdmin)
admin.site.site_header = "激活平台系统"
admin.site.site_title = "后台管理"
admin.site.index_title = "激活管理"

