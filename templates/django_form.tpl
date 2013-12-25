{% extends 'base.tpl' %}
{% block side %}
{% endblock %}
{% block context %}
<form method='post' action='/django_form/'>
    {% csrf_token %}
    {{ form.as_table }}
    
    <input type="submit" value="create">
</form>
{% endblock %}