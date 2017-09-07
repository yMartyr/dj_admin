#!/user/bin/env python
# -*- coding:utf-8 -*-

from django.template import Library
from django.utils.safestring import mark_safe
from types import FunctionType

register=Library()

# def checkbox(pk):
#     return mark_safe("<input type='checkbox' value=%s>"%pk)
#
#
# def edit(v):
#
#     path=None
#     return mark_safe("<a href='%s' >编辑</a>"%path)
#不在这里写

def table_head(list_display):
    li=[]
    for row in list_display:
        li.append(row)
    return li


def table_body(result_list,list_display,mcadmin_obj):
    for row in result_list:
        # li=[]
        # # li.append (checkbox (res.pk))    #pk即主键
        # for ele in list_display:
        #
        #     li.append(getattr(row,ele))
        # yield li
        yield [ele(mcadmin_obj,row) if isinstance(ele,FunctionType) else getattr(row,ele) for ele in list_display]
        # 如果ele是函数名，会将row对象传过去

@register.inclusion_tag("mc/md.html")   #返回的参数传给前台
def func(result_list,list_display,mcadmin_obj):
    th=table_head(list_display)
    tb=table_body(result_list,list_display,mcadmin_obj)
    # print(v)

    return {'tb':tb,'th':th}
