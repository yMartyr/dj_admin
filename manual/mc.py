#!/user/bin/env python
# -*- coding:utf-8 -*-

print('123')

from manual.service import v1
from manual import models
from manual.service.v1 import BaseManualAdmin
from django.utils.safestring import mark_safe
class BaseUserInfo(BaseManualAdmin):

    def checkbox(self,obj):
        return mark_safe ("<input type='checkbox' value=%s>" % obj.pk)

    def edit(self,obj):
        """
        编辑
        self: #<manual.mc.BaseUserInfo object at 0x0000025425664BE0>,从前台传过来的对象
        obj : for循环显示table每一条记录所对应的对象。这里用type(obj)拿到它的父类
        :return:
        """
        #方式一：obj
        # print("type(obj):",type(obj))
        # print(type(obj)._meta.model_name)
        # print(type(obj)._meta.app_label)
        # print(type(obj).site.namespace)


        #方式二：self
        # print(self.model_class._meta.model_name)
        # print(self.model_class._meta.app_label)
        # print(self.site.namespace)
        model_name=self.model_class._meta.model_name
        app_label=self.model_class._meta.app_label
        namespace=self.site.namespace
        path="/{0}/{1}/{2}/{3}".format(namespace,model_name,app_label,obj.pk)
        edit_url="<a href='%s'>编辑</a>"%path
        return mark_safe(edit_url)

    list_display=[checkbox,'id','uname','email',edit]




class BaseRole(BaseManualAdmin):
    list_display=['id','title']


v1.site.register(models.UserInfo,BaseUserInfo)
v1.site.register(models.Role,BaseRole)