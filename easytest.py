# -*- coding:utf-8 -*-
#!/usr/bin/env python
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "osc.settings")



from firstapp.models import OSCUser, Book, Cat

# 初始化若干数据
# -------------
yangfan = OSCUser.objects.create(name=u'yangfan',sex=True,age=21,email=u'freedom_7@yeah.net')

wangrui = OSCUser()
wangrui.name = u'wangrui'
wangrui.sex  = True
wangrui.email= u'wangruikernel@gmail.com'
wangrui.blog = u'http://www.shunix.com'
wangrui.age  = 18
wangrui.save()

sangbo = OSCUser.objects.create(name=u'sangbo',age=20,sex=True,email=u'xxxx@163.com')
lady1  = OSCUser.objects.create(name=u'lady1',age=19,sex=False,email=u'xxxx@163.com')

# --------------

book = Book.objects.create(book_name=u'The Django Book',owner=yangfan)

book.learner.add(yangfan)
book.learner.add(sangbo)

# ---------------

cat  = Cat.objects.create(owner=yangfan)