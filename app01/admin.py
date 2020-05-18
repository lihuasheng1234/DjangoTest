from django.contrib import admin
from app01 import models
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    list_filter = ('name',)

    class Meta:
        model = models.Userinfo
        fields = ('email',)


admin.site.register(models.Userinfo,UserInfoAdmin)

