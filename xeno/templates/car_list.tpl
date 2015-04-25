{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}
<link href="style/dash_style.css" rel="stylesheet" />


<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
                <div id="pageDescription" class="underline">Cars Offered</div>
    </div>
    {% with messages = get_flashed_messages() %}
    {% if messages %}
    <h4 class="message_flash">{{ messages[0] }}</h4>
    {% endif %}
    {% endwith %}
    <div class="carList">
        {% for car in cars %}
        <div class="carWrapper custC" style="
          background:
            linear-gradient( rgba(255, 255, 255, 0) 50%,
            rgba(0, 0, 0, 0.65) 100%),
            url(/images/acura_concept.jpg);
            background-size: cover;
        ">
            <span class="car_title">{{car["year"]|string + " " + car["make"] + " " + car["model"] }}</span>
        </div>
    {% endfor %}
    </div>
</div>

{% endblock %}