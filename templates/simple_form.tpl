{% extends 'base.tpl' %}
{% block side %}
{% endblock %}
{% block context %}
<form method='post' action='/simple_form/'>
    {% csrf_token %}
    <input name="name" type="text" value="狂拽酷炫屌炸天"> </br>   
    <input name="sex" type="text"></br>
    <input name="blog" type="text"></br>
    <input name="email" type="text" placeholder="example:xxx@163.com"></br>
    <input name="blog" type="text"></br>
    <input type="submit" value="create">
</form>
{% endblock %}