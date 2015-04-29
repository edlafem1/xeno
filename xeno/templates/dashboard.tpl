<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"/>

    <link href="/style/dashboard_style.css" rel="stylesheet"/>
    <link href="/style/style.css" rel="stylesheet"/>
    <link href="/style/button.css" rel="stylesheet"/>

    <script src="//code.jquery.com/jquery-1.10.2.js"></script>
    <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
    <script src="/scripts/konami.js"></script>

    <base href="/"/>
</head>

<body>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <h4 class="message_flash">{{ messages[0] }}</h4>
        {% endif %}
    {% endwith %}
{% block body %}{% endblock %}
</body>


</html>