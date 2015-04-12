<!DOCTYPE html>
<html>
    <head>
        <link href="style/style.css" rel="stylesheet" />
        <link href="style/button.css" rel="stylesheet" />
    </head>
    <body>
    <div class="mainWrapper">
        <div class="main">
            <h2 class="name">&nbsp;XENO</h2>
            {% with messages = get_flashed_messages() %}
            {% if messages %}
            <h4 class="message_flash">{{ messages[0] }}</h4>
            {% endif %}
            {% endwith %}
            <!-- Placeholder for view. Views get dynamically injected here -->
            {% block body %}{% endblock %}


            <table class="searchTable">
                <tr>
                    <td class="center searchTable">
                        <a href="login">Login</a>
                    </td>
                    <td class="center searchTable">
                        <a href="search">Search</a>
                    </td>
                    <td class="center searchTable">
                        <a href="sign_up">Sign up</a>
                    </td>
                </tr>
            </table>
        </div>
    </div>
    <script src="scripts/konami.js"></script>
    </body>
</html>