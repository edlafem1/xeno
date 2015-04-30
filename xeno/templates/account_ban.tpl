{% extends "dashboard.tpl" %}
{% block body %}

{% if admin %}
{% include "menu.tpl" %}


<link href="style/profile.css" rel="stylesheet" />
<link href="style/dash_style.css" rel="stylesheet" />

<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
                <div id="pageDescription" class="underline">{{user_data["firstname"]}} {{user_data["lastname"]}}'s Profile</div>
                <div class="switch" align="right">
                    Enabled:
                    <input id="toggle-{{ i }}" class="toggle toggle-round-flat" type="checkbox">
                    <label for="toggle-{{ i }}"></label>
                </div>
    </div>
    
    <div class="profile_container">
        <div class="personal boxed">
            <img src="images/profiles/blank_face.jpeg" class="propic">

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
                <div class="carWrapper custC" style="
                    background:
                        linear-gradient( rgba(255, 255, 255, 0) 50%,
                        rgba(0, 0, 0, 0.65) 100%),
                        url(/images/acura_concept.jpg);
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
                </div>
            </div>
        </div>
        <div class="user_activity">
            <div class="underline">Recent Activity</div>
            <div class="activity_details">
                <div class="activity_event">

                </div>
                <div class="activity_event">

                </div>
                <div class="activity_event">

                </div>
                <div class="activity_event">

                </div>
                <div class="activity_event">

                </div>
                <div class="activity_event">

                </div>
                <div class="activity_event">

                </div>
                <div class="activity_event">

                </div>
                <div class="activity_event">

                </div>
                <div class="activity_event">

                </div>
                <div class="activity_event">

                </div>

            </div>
        </div>
    </div>
    
</div>

{% else %}
{% include "menu.tpl" %}
<div>
Error! You do not have permission to view this page.
</div>
{% endif %}
{% endblock %}