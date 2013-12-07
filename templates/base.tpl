<html>
{% include 'head.tpl' %}
<body>
{% block side %}
{% include 'side.tpl' %}
{% endblock %}
{% block context %}
{% include 'container.tpl' %}
{% endblock %}
{% include 'footer.tpl' %}
</body>
</html>