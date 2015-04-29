{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}
<link href="/style/dash_style.css" rel="stylesheet" />

<div class="fadeInUp">

    
    <div id="featuredCarsTitleWrapper">
                <div id="featuredCarsTitle" class="underline">Featured Cars</div>
    </div>

<!--
    <div class="carList">
        {% for car in featured_cars %}
        <div class="carWrapper">
                <div id="carPic">
                    <!--{{car["id"]|string + ".jpg"}} for img filename -a->
                </div>
                <div class="carName">
                    {{car["year"]|string + " " + car["make"] + " " + car["model"] }}
                </div>
        </div>
    {% endfor %}
    </div>
-->

    <div class="carList">
        {% for car in featured_cars %}
        <div class="carWrapper custC" style="
          background:
            linear-gradient( rgba(255, 255, 255, 0) 50%,
            rgba(0, 0, 0, 0.65) 100%),
            url(/images/cars/{{ car["id"] }}_main.pic);
            background-size: cover;
        ">
            <span class="car_title">{{car["year"]|string + " " + car["make"] + " " + car["model"] }}</span>
        </div>
        {% endfor %}
    </div>

    <div id="newCarsTitleWrapper">
                <div id="newCarsTitle" class="underline">New Cars</div>
    </div>
    <div class="carList">
        {% for car in new_cars %}
        <div class="carWrapper custC" style="
          background:
            linear-gradient( rgba(255, 255, 255, 0) 50%,
            rgba(0, 0, 0, 0.65) 100%),
            url(/images/cars/{{ car["id"] }}_main.pic);
            background-size: cover;
        ">
            <span class="car_title">{{car["year"]|string + " " + car["make"] + " " + car["model"] }}</span>
        </div>
    {% endfor %}
    </div>
</div>
{% endblock %}