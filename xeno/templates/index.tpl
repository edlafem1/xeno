<!DOCTYPE html>
<html>
    <head>
        <link href="style/style.css" rel="stylesheet" />
    </head>
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
                    <td class="left searchTable">
                        <a href="login">Login</a>
                    </td>
                    <td class="searchTable">
                        <a href="search">Search</a>
                    </td>
                    <td class="right searchTable">
                        <a href="sign_up">Sign up</a>
                    </td>
                </tr>
            </table>
        </div>
    </div>
    <!--
    <script src="scripts/angular.min.js"></script>
    <script src="scripts/angular-route.min.js"></script>
    <script src="scripts/module.js"></script>
    -->
    <script src="scripts/konami.js"></script>

<!-- How to do a bottom menu bar that doesn't move
    <body style="padding:0;">
        <div style="position:fixed; width:100%; height:70px; padding:5px; bottom:0px; ">
            test content :D
        </div>
        Content Here
    </body>
-->
    
</html>