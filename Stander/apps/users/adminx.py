# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import UserProfile
from  xadmin.plugins.auth import  UserAdmin

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GloabalSettings(object):
    site_title = "游泳防溺水系统"
    site_footer = "游泳防溺水系统"
    menu_style = "accordion"

class UserAdmin(object):
    list_display = ['username', 'nick_name', 'last_login', 'email']
    search_fields = ['username', 'nick_name', 'last_login', 'email']
    list_filter = ['username', 'nick_name', 'last_login', 'email']


# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GloabalSettings)