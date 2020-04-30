# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.
class UserProfile(AbstractUser):


    nick_name = models.CharField(max_length=50,verbose_name=u'姓名')
    birthday = models.DateField(null=True,blank=True,verbose_name=u'生日',default='2010-01-01')
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default=u"女",verbose_name=u'性别')
    address = models.CharField(max_length=100,default=u'',verbose_name=u'地址')
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name=u'手机号')
    image = models.ImageField(upload_to="image/%Y/%m",default=u'image/default.png',max_length=100,verbose_name=u'头像')
    # birthday = models.DateField(null=True, blank=True, verbose_name=u'生日', default='2010-01-01')
    # is_staff = models.BooleanField(default=False,verbose_name=u'是否为老师')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username