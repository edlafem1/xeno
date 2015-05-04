{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}
<link href="/style/dash_style.css" rel="stylesheet" />

<div class="fadeInUp">

    <div id="return_car_wrapper">
        <form id="return_car_form" action="" method="POST">
            <button class="button button-border-primary button-rounded" style="color: red; border: 2px solid red;">Return Bugatti Veyron Super Sport</button>
        </form>
    </div>
    
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
        <a href="/car/{{ car['id'] }}">
        <div class="carWrapper custC" style="
          background:
            linear-gradient( rgba(255, 255, 255, 0) 50%,
            rgba(0, 0, 0, 0.65) 100%),
            url(/images/cars/{{ car["id"] }}_main.pic);
            background-size: cover;
        ">
            <span class="car_title">{{car["year"]|string + " " + car["make"] + " " + car["model"] }}</span>
        </div>
        </a>
        {% endfor %}
    </div>

    <div id="newCarsTitleWrapper">
                <div id="newCarsTitle" class="underline">New Cars</div>
    </div>
    <div class="carList">
        {% for car in new_cars %}
        <a href="/car/{{ car['id'] }}">
        <div class="carWrapper custC" style="
          background:
            linear-gradient( rgba(255, 255, 255, 0) 50%,
            rgba(0, 0, 0, 0.65) 100%),
            url(/images/cars/{{ car["id"] }}_main.pic);
            background-size: cover;
        ">
            <span class="car_title">{{car["year"]|string + " " + car["make"] + " " + car["model"] }}</span>
        </div>
        </a>
    {% endfor %}
    </div>
    
    <div id="waitlist_wrapper">
        <form id="waitlist_form" action="" method="POST">
            <button class="button button-border-primary button-rounded">Join the waitlist for a random car!</button>
        </form>
    </div>
    
</div>
{% endblock %}