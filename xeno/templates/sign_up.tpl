{% extends "index.tpl" %}
{% block body %}
<div class="container">
    <h2>Sign Up</h2>
    <form action="{{ url_for('sign_up') or 'sign_up' }}" method="POST">
        <br />
        <input type="text" placeholder="{{ name or 'Name' }}" value="{{ name or '' }}" name="full_name" required />
        <br />
        <br />
        <!-- password match on ^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{4,8}$
        requires one lower case letter, one upper case letter, one digit, 6-13 length, and no spaces
        -->
        <!--pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{4,8}$"-->
        <input type="password" id="password" placeholder="Password" name="password" required />
        <br />
        <br />
        <input type="password" id="confirm_password" placeholder="Re-Enter Password" name="password2" required />
        <br />
        <br />
        <!--pattern="^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$"-->
        <input type="text" placeholder="{{ email or 'Email' }}" value="{{ email or '' }}" name="email" required />
        <br />
        <div id="login_buttom_wrapper">
            <button class="button button-border-primary button-rounded">Sign Up</button>
        </div>
    </form>
    
</div>

<script type="text/javascript">
    var password = document.getElementById("password")
    var confirm_password = document.getElementById("confirm_password");

function validatePassword() {
    if(password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_password.setCustomValidity('');
    }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;
</script>
{% endblock %}


<!-- In case something doesnt work, here's another way to preserver input values

<input type="text" {% if email|length > 0 %}
               value="{{ email }}"
               {% else %}
               placeholder="Email"
               {% endif %}
               name="email" />

-->