{% extends "index.tpl" %}
{% block body %}
<div class="container">
    <h2>Login</h2>
    <br />
    <form action="{{ url_for('login') or 'login' }}" method="POST" autocomplete="off">
        <input type="hidden" name="next" value="{{ next or '' }}">
        <input type="text" placeholder="Email Address" name="username" value="{{ username or '' }}">
        <br />
        <br />
        <input type="password" placeholder="Password" name="password">
        <br />
        <div id="login_buttom_wrapper">
            <button class="button button-border-primary button-rounded">Login</button>
        </div>
<!--        <button type="submit">Login</button>-->
    </form>
    {% if error %}
        <p class="error"><strong>Error:</strong> {{ error }}
    {% endif %}
    <br />
    
    <br />
    
</div>
{% endblock %}