<html>
<head>
<title>
这是标题</title>
    <link href="http://v2.bootcss.com/assets/css/bootstrap.css" rel="stylesheet">
    <link href="http://v2.bootcss.com/assets/css/bootstrap-responsive.css" rel="stylesheet">
</head>
<body>
<h1>欢迎来到开源社区</h1>
<h2>---Django框架入门</h2>

<p>Django 在新一代的 Web框架 中非常出色,为什么这么说呢?
为回答该问题,让我们考虑一下不使用框架设计 Python 网页应用程序的情形。 贯穿整本书,我们多次展示不
使用框架实现网站基本功能的方法,让读者认识到框架开发的方便。 (不使用框架,更多情况是没有合适的框
架可用。 最重要的是,理解实现的来龙去脉会使你成为一个优秀的web开发者。)
使用Python开发Web,最简单,原始和直接的办法是使用CGI标准,在1998年这种方式很流行。 现在从应用
角度解释它是如何工作: 首先做一个Python脚本,输出HTML代码,然后保存成.cgi扩展名的文件,通过浏览
器访问此文件。 就是这样。</p>

<button class="btn btn-primary">我是一个按钮</button>
<p></br></p>
<form action="./" method="GET">
    <input type="text" placeholder="我是一个输入框">
</form>

{% if name %}
<p>欢迎{{name}}</p>
{% else %}
<p>你没有给我任何数据耶，你在卖萌吗？</p>
{% endif %}


<table class="table">
<tr><th>序号</th><th>内容</th></tr>
<tbody>
{% for i in list %}
<tr><td>这是第{{i}}条数据</td><td>这是相同的内容</td></tr>
{% endfor %}
</tbody>
</table>


<div></div>

</body>
</html>
