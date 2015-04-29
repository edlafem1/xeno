<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        
        <link href="/style/dashboard_style.css" rel="stylesheet" />
        <link href="/style/style.css" rel="stylesheet" />
        <link href="/style/button.css" rel="stylesheet" />
        
        <script src="/scripts/konami.js"></script>

        <base href="/" />
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