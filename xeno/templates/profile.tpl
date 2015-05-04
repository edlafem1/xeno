{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}


<link href="style/profile.css" rel="stylesheet" />
<link href="style/dash_style.css" rel="stylesheet" />

<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
                <div id="pageDescription" class="underline">{{user_data["firstname"]}} {{user_data["lastname"]}}'s Profile</div>
    </div>

    <div class="profile_container">
        <div class="personal boxed">
            <img id="photo" src="images/profiles/{{ user_data["profile_pic"] }}" class="propic">
            
            <form id="photo_form" action="/profile" enctype="multipart/form-data" method="POST">
                <input type="file" id="file" name="photo" style="display: none;" />
            </form>
            
            <div class="user_details">
                <ul>
                    <li>Joined {{ user_data["date_joined"] }}</li>
                    <li>{{ user_data["email"] }}</li>
                    <li>Total Credits: {{ user_data["credits"] }}</li>
                    {% if user_data["suspended_until"]|length > 0 %}
                        <li>Suspended Until: Never</li>
                    {% else %}
                        <li>Active User</li>
                    {% endif %}
                </ul>
            </div>
            <div class="favorite_car">
                <span class="fav_car_label">Favorite Car:</span>
                <div style="height: 85%; margin-top: .8em;">
                    <a href="/car/{{ fav_car['id'] }}">
                <div class="carWrapper custC" style="
                    background:
                        linear-gradient( rgba(255, 255, 255, 0) 50%,
                        rgba(0, 0, 0, 0.65) 100%),
                        url(/images/cars/{{ fav_car["id"] }}_main.pic);
                        background-size: cover;
                        background-repeat: round;
                        min-height: 0;
                        height: 100%;
                        width: 100%;
                        margin: 0;
                ">
                    <!--django stuff car["year"]|string + " " + car["make"] + " " + car["model"] -->
                    <span class="car_title">
                        {% if fav_car != None and fav_car|length > 0 %}
                            {{ fav_car["year"]|string + " " + fav_car["make"] + " " + fav_car["model"] }}
                        {% else %}
                            2015 Ford Focus
                        {% endif %}
                    </span>
                </div>
                </a>
                </div>
            </div>
        </div>
        <div class="user_activity">
            <div class="underline">Recent Activity</div>
            <div class="activity_details">
                
                {% for i in range(activity | length) %}
                
                <a href="/car/{{ activity[i]['car'] }}" style="color:white; font-weight: normal;">
                    <div class="activity_event">
                        {{ activity[i]['date'] }}: {{ activity[i]['type'] }}
                        <div>
                        {{recent_cars[i]["year"]|string + " " + recent_cars[i]["make"] + " " + recent_cars[i]["model"] }}
                        </div>
    <!--                        <div class="carWrapper custC" style="
                              background:
                                linear-gradient( rgba(255, 255, 255, 0) 50%,
                                rgba(0, 0, 0, 0.65) 100%),
                                url(/images/cars/{{ activity[i]['car'] }}_main.pic);
                                background-size: cover;
                            ">
    <!--                            <span class="car_title">{{recent_cars[i]["year"]|string + " " + recent_cars[i]["make"] + " " + recent_cars[i]["model"] }}</span>-->
    <!--                        </div>-->

                    </div>
                </a>
                {% endfor %}
            </div>
        </div>
    </div>
    
<!--  Scripts to make clicking the picture change the photo  -->
    <script type="text/javascript">
        $("#photo").click(function(){
            $("#file").trigger("click");
        });
        document.getElementById("file").onchange = function() {
            document.getElementById("photo_form").submit();
        };
    </script>
    
    
</div>
{% endblock %}