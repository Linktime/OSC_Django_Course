# -*- coding:utf-8 -*-
from firstapp.models import OSCUser
from django import forms

class OSCUserForm(forms.Form):
    name = forms.CharField(max_length=30,label=u'姓名')
    sex = forms.BooleanField()
    email = forms.EmailField()
    blog = forms.URLField(label=u'博客',initial='blog.shuosc.org')
    age = forms.IntegerField()
    other = forms.CharField(widget=forms.Textarea(attrs={"class":"xxx"}))

    def clean_age(self):
        age = self.cleaned_data['age']
        if age<18:
            raise forms.ValidationError("根据未成年保护法，请您自觉离开!")
        else :
            return age

class OSCUserModelForm(forms.ModelForm):
    class Meta:
        model = OSCUser
        exclude = ('blog')