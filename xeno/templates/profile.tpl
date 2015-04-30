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























<!--
    <table cellspacing=55 class="fadeInUp">
        <tr>
            <td>
                <div class="boxed">
                    <img src="images/blank_face.jpeg" style="width:304px;height:228px">
                </div>
            </td>
            <td colspan="2">
                <table class="fadeInUp">
                    <tr>
                        <td colspan="2">
                            <div class="underline">
                                Cars {{firstname}} Reviewed
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <img class="carPic" src="images/bugatti.jpg" style="width:150px;height:150px;border:1px solid gold">
                        </td>
                        <td>
                            The car is wayy too fast
                        </td>
                    </tr>
                </table>
            </td>
            <tr>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </tr>

    </table>    
    -->
    
</div>
{% endblock %}