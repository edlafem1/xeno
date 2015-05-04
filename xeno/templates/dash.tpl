{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}
<link href="/style/dash_style.css" rel="stylesheet" />

<div class="fadeInUp">

<!--
    {% for i in range(reserved_car_data | length) %}
    <div id="return_car_wrapper">
        <form id="return_car_form_{{ i }}" action="/return" method="POST">
            <input name="reservation_id" type="hidden"
                   value="{{ reserved_car_data[i]['id'] }}"/>
            <input name="car_id" type="hidden"
                   value="{{ reserved_car_data[i]['for_car'] }}" />
            <button class="button button-border-primary button-rounded" style="color: red; border: 2px solid red;">Return {{ reserved_car_names[i] }}</button>
        </form>
    </div>
    {% endfor %}
-->
    
    {% for i in range(reserved_car_data | length) %}
    
    <!-- If the car is reserved today but not checked out -->
    {% if reserved_car_status[i] == '1' %}
    <div id="return_car_wrapper">
        <form id="return_car_form_{{ i }}" action="/claim" method="POST">
            <input name="car_id" type="hidden"
                   value="{{ reserved_car_data[i]['for_car'] }}" />
            <button class="button button-border-primary button-rounded" style="color: lawngreen; border: 2px solid lawngreen;">Claim {{ reserved_car_names[i] }}</button>
        </form>
    </div>
    
    {% else %} <!-- If the car is reserved today and checked out -->
    <div id="return_car_wrapper">
        <form id="return_car_form_{{ i }}" action="/return" method="POST">
            <input name="reservation_id" type="hidden"
                   value="{{ reserved_car_data[i]['id'] }}"/>
            <input name="car_id" type="hidden"
                   value="{{ reserved_car_data[i]['for_car'] }}" />
            <button class="button button-border-primary button-rounded" style="color: red; border: 2px solid red;">Return {{ reserved_car_names[i] }}</button>
        </form>
    </div>
    {% endif %}
    {% endfor %}
    
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <h4 class="message_flash">{{ messages[0] }}</h4>
        {% endif %}
    {% endwith %}
    
    <div id="featuredCarsTitleWrapper">
                <div id="featuredCarsTitle" class="underline">Featured Cars</div>
    </div>

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
        <form id="waitlist_form" action="/waitlist" method="POST">
        {% if waiting %}
            <input name="join" type="hidden" value="0"/>
            <button class="button button-border-primary button-rounded" style="color: red; border: 2px solid red;">Remove me from the waitlist.</button>
        {% else %}
            <input name="join" type="hidden" value="1"/>
            <button class="button button-border-primary button-rounded">Join the waitlist for a random car!</button>
        
        {% endif %}
        </form>
    </div>
    
</div>
{% endblock %}