{% extends 'base.tpl' %}
{% block side %}
{% endblock %}
{% block context %}
<form method='post' action='/django_modelform/'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="create">
</form>
{% endblock %}