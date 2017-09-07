from django.apps import AppConfig


class ManualConfig(AppConfig):
    name = 'manual'

    def ready(self):   #执行apps时，会自动加载ready
        super(ManualConfig,self).ready()

        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('mc')   #会自动加载每个apps中的mc.py文件