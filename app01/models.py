from django.db import models
from MyDjangoTestProject import settings
# Create your models here.


class Userinfo(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)
    email = models.EmailField()
    selfpic = models.FileField(verbose_name='头像',upload_to=settings.IMG_DISK_SAVE_PATH,default=settings.IMG_DISK_SAVE_PATH)






