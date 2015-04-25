{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}
<link href="style/dash_style.css" rel="stylesheet" />

<div class="fadeInUp">

    
    <div id="featuredCarsTitleWrapper">
                <div id="featuredCarsTitle" class="underline">Featured Cars</div>
    </div>
    <!--
    <div class="carList">
        <div class="carWrapper">
            <div id="carPic">
            </div>
            <div class="carName">
                Maserati
            </div>    
        </div>
        <div class="carWrapper">
            <div id="carPic">
            </div>
            <div class="carName">
                Maserati
            </div>
        </div>
        <div class="carWrapper">
            <div id="carPic">
            </div>
            <div class="carName">
                Maserati
            </div>    
        </div>
        <div class="carWrapper">
            <div id="carPic">
            </div>
            <div class="carName">
                Maserati
            </div>    
        </div>
    </div>
    -->

    <div class="carList">
        {% for car in featured_cars %}
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


    <div id="newCarsTitleWrapper">
                <div id="newCarsTitle" class="underline">New Cars</div>
    </div>
    <div class="carList">
        {% for car in new_cars %}
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