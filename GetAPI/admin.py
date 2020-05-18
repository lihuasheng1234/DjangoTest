from django.contrib import admin

# Register your models here.

from GetAPI.models import userinfo


class AuthorAdmin(admin.ModelAdmin):
    fields = ['name','email']
admin.site.register(userinfo)

