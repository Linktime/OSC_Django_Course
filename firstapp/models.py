# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class Cat(models.Model):
    owner = models.ForeignKey('OSCUser')


class OSCUser(models.Model):
    name = models.CharField(max_length=30, db_index=True,verbose_name=u'姓名')
    sex = models.BooleanField()
    email = models.EmailField()
    blog = models.URLField(null=True, blank=True,verbose_name=u'博客')
    age = models.IntegerField()

    def __unicode__(self):
        return '%s   %s' % (self.name, self.age)


class Book(models.Model):
    book_name = models.CharField(max_length=30)
    owner = models.ForeignKey(OSCUser, related_name='book_owner')
    learner = models.ManyToManyField(OSCUser, related_name='book_learner')

    def __unicode__(self):
        return self.book_name
