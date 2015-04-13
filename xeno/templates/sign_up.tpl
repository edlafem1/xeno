{% extends "index.tpl" %}
{% block body %}
<div class="container">
    <h2>Sign Up</h2>
    <form action="{{ url_for('sign_up') or 'sign_up' }}" method="POST">
        <br />
        <input type="text" placeholder="{{ name or 'Name' }}" value="{{ name or '' }}" name="full_name" />
        <br />
        <br />
        <!-- password match on ^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{4,8}$
        requires one lower case letter, one upper case letter, one digit, 6-13 length, and no spaces
        -->
        <input type="password" placeholder="Password" name="password"/>
        <br />
        <br />
        <input type="password" placeholder="Re-Enter Password" name="password2"/>
        <br />
        <br />
        <input type="text" placeholder="{{ email or 'Email' }}" value="{{ email or '' }}" name="email" />
        <br />
        <div id="login_buttom_wrapper">
            <button class="button button-border-primary button-rounded">Sign Up</button>
        </div>
    </form>
    
</div>
{% endblock %}


<!-- In case something doesnt work, here's another way to preserver input values

<input type="text" {% if email|length > 0 %}
               value="{{ email }}"
               {% else %}
               placeholder="Email"
               {% endif %}
               name="email" />

-->