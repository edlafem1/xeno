{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}

<head>
    <link href="style/profile.css" rel="stylesheet" />
</head>

<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
                <div id="pageDescription" class="underline">Profile</div>
    </div>

    <table cellspacing=25 class="fadeInUp">
        <tr>
            <td>
                <div class="boxed">
                    <img src="images/blank_face.jpeg" style="width:304px;height:228px">
                </div>
            </td>
            <td>
                <div class="underline">
                    Cars {{firstname}} Reviewed
                </div>
                <img class="carPic" src="images/bugatti.jpg" style="width:150px;height:150px;border:1px solid gold">
                <td>
                    The car is wayy too fast
                </td>
            </td>
            <tr>
                <td>
                {{firstname}} {{lastname}}
                </td>
            </tr>
        </tr>
        <tr>
            
        </tr>
    </table>    
    
    
</div>
{% endblock %}