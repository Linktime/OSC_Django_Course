{% extends 'base.tpl' %}
{% block context %}
<p>这是被重写的地方</p>
今天是{{time.month}}月{{time.day}}号
模板标签{{time|date:"G:i"}}
{% endblock %}