# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template,Context
from django.shortcuts import render_to_response
from datetime import datetime

from django.template import RequestContext

from firstapp.models import OSCUser
from firstapp.forms import OSCUserForm,OSCUserModelForm

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
    f = open("F:\\Freedom\\ces\\osc\\templates\\index.tpl","r") # 更改站点目录时必须更改
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

def simple_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        email = request.POST.get('email')
        blog = request.POST.get('blog')
        age = request.POST.get('age')
        # Do something

        # osc_user = OSCUser.objects.create(name=name,sex=sex,email=email,blog=blog,age=age)
        try :
            osc_user = OSCUser.objects.create(**request.POST)
        except OSCUser.DoesNotExist:
            pass
        return render_to_response('success.tpl')
    else :
        return render_to_response('simple_form.tpl',context_instance=RequestContext(request))

def django_form(request):
    if request.method == 'POST':
        form = OSCUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sex = form.cleaned_data['sex']
            email = form.cleaned_data['email']
            blog = form.cleaned_data['blog']
            age = form.cleaned_data['age']
            try :
                osc_user = OSCUser.objects.create(**request.GET)
            except OSCUser.DoesNotExist:
                pass
            return render_to_response('success.tpl')
    else:
        form = OSCUserForm()
    return render_to_response('django_form.tpl',{'form':form},context_instance=RequestContext(request))

def django_modelform(request):
    if request.method == 'POST':
        form = OSCUserModelForm(request.POST)
        if form.is_valid():
            osc_user = form.save(submit=False)
            return render_to_response('success.tpl')
    else:
        form = OSCUserModelForm()
        return render_to_response('django_modelform.tpl',{'form':form},context_instance=RequestContext(request))