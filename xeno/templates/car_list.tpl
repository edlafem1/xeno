{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}
<link href="style/dash_style.css" rel="stylesheet" />


<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
                <div id="pageDescription" class="underline">Cars Offered</div>
    </div>
    <div class="carList">
        {% for car in cars %}
        <div class="carWrapper">
                <div id="carPic">
                    <!--{{car["id"]|string + ".jpg"}} for img filename -->
                </div>
                <div class="carName">
                    {{car["year"]|string + " " + car["make"] + " " + car["model"] }}
                </div>
        </div>
    {% endfor %}
    </div>
</div>

{% endblock %}