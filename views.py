# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template,Context
from django.shortcuts import render_to_response
from datetime import datetime

def index(request):
    # 硬编码

    #s = u"你好，开源社区"
    s = u"<font color='red'><b>你好，开源社区</b></font>"
    return HttpResponse(s)

def diy_tpl(request):
    # 模板内嵌在views中

    #t1 = Template("你好，！")
    t2 = Template("你好，{{name}}")
    c = Context({"name":"开源"})
    return HttpResponse(t2.render(c))

def load_tpl(request):
    # 用IO流读取
    f = open("F:\\Freedom\\ces\\osc\\templates\\index.tpl","r")
    t = Template(f.read())
    f.close()
    mylist = [i for i in range(1,11)]
    c = Context({"name":"张三","list":mylist})
    #c = Context()
    return HttpResponse(t.render(c))

def simple_tpl(request):
     # 在settings中的TEMPLATES_DIR设定好模板目录，使用Django封装好的函数直接读取模板

    time = datetime.now()
    # t = get_template("index.tpl")
    # c = Context({"name":"李四"}) 
    # return HttpResponse(t.render(c))
    #还有更简洁的吗?

    return render_to_response('child.tpl',{'list':[i for i in range(10)],'time':time})
