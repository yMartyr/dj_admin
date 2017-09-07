#!/user/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse,render
from manual import models

class BaseManualAdmin(object):
    list_display="__all__"

    def __init__(self,model_class,site):
        self.model_class=model_class
        self.site=site


    @property
    def urls(self):
        from django.conf.urls import url,include
        info=self.model_class._meta.app_label,self.model_class._meta.model_name


        urlpatterns=[
            url(r'^$',self.changelist_view,name='%s_%s_changelist'%info),
            url(r'^add/$',self.add_view,name='%s_%s_add'%info),
            url(r'^(.+)/delete/$',self.delete_view,name='%s_%s_delete'%info),
            url(r'^(.+)/change/$',self.change_view,name='%s_%s_change'%info),
        ]
        print(urlpatterns)
        return urlpatterns

    def changelist_view(self,request):
        # info=self.model_class._meta.app_label,self.model_class._meta.model_name
        # data="%s_%s_change"%info
        # print(data)
        # return HttpResponse (data)
        result_list = self.model_class.objects.all()
        context={
            "result_list":result_list,
            "list_display":self.list_display,
            "mcadmin_obj":self,
        }

        print(context)
        return render(request,'mc/change_list.html',context)


    def add_view(self,request):
        info=self.model_class._meta.app_label,self.model_class._meta.model_name
        data="%s_%s_add"%info
        return HttpResponse(data)


    def delete_view(self,request):
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = "%s_%s_delete" % info
        return HttpResponse (data)

    def change_view(self,request):
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = "%s_%s_change" % info
        return HttpResponse (data)

class ManualSite(object):
    def __init__(self):
        self._registry={}
        self.namespace='manual'
        self.app_name='manual'

    def register(self,model_class,xx=BaseManualAdmin):
        """

        :param model_class: models模板中的类名，如UserInfo，UserGroup
        :param xx:
        :return:
        """
        self._registry[model_class]=xx(model_class,self)
        # _registry={
        #     'userinfo':BaseUserInfo('userinfo',ManualSite_obj)

        # }


    def get_urls(self):
        from django.conf.urls import url,include
        ret=[
            # url(r'^login/',self.login,name='login'),
            # url(r'^/manual/k1/',self.login),
        ]
        for model_cls,mc_admin_obj in self._registry.items():
            # mc_admin_obj 是BaseManualAdmin类的对象
            app_label=model_cls._meta.app_label
            model_cls=model_cls._meta.model_name

            # print(app_label,model_cls)
            # print(mc_admin_obj)
            # ret.append(url(r'^%s/%s/'%(app_label,model_cls),self.login))   #http://127.0.0.1:8000/manual/manual/k1/
            ret.append(url(r'%s/%s/'%(app_label,model_cls),include(mc_admin_obj.urls)))
        return ret


    @property
    def urls(self):
        return self.get_urls(),self.app_name,self.namespace


    def login(self,request):

        return HttpResponse('login')

site=ManualSite()