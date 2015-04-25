{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}


<link href="style/profile.css" rel="stylesheet" />
<link href="style/dash_style.css" rel="stylesheet" />

<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
                <div id="pageDescription" class="underline">{{firstname}} {{lastname}}'s Profile</div>
    </div>

    <div class="profile_container">
        <div class="personal boxed">
            <img src="images/blank_face.jpeg" class="propic">

            <div class="user_details">
                <ul>
                    <li>Joined 04/25/2015</li>
                    <li>admin@xeno.com</li>
                    <li>Total Credits: 568</li>
                    <li>Suspended Until: Never</li>
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
                    <span class="car_title">2015 Ford Focus</span>
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