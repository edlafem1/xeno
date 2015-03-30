{% extends "index.tpl" %}
{% block body %}
<div class="container">
    <h2>Login</h2>
    <br />
    <form action="" method="POST">
        <input type="text" placeholder="Username" name="username" value="{{ request.form.username }}">
        <br />
        <br />
        <input type="password" placeholder="Password" name="password" value="{{ request.form.password }}">
        <br />
        <button type="submit">Login</button>
    </form>
    {% if error %}
        <p class="error"><strong>Error:</strong> {{ error }}
    {% endif %}
    <br />
    
    <br />
    
</div>
{% endblock %}