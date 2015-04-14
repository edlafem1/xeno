{% extends "dashboard.tpl" %}
{% block body %}

{% if admin %}
{% include "menu.tpl" %}

<head>
    <link href="style/profile.css" rel="stylesheet" />
</head>

<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
                <div id="pageDescription" class="underline">Profile</div>
    </div>

    <table cellspacing=55 class="fadeInUp">
        <tr >
            <td>
                <div class="boxed">
                    <img src="images/blank_face.jpeg" style="width:304px;height:228px">
                </div>
            </td>
            <td></td>
            <td>
                Enabled: <div class="switch">
                    <input id="toggle-{{ i }}" class="toggle toggle-round-flat" type="checkbox">
                    <label for="toggle-{{ i }}"></label>
                </div>
            </td>
            <tr>
                <td >
                {{firstname}} {{lastname}}
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
                                This car is wayy too fast!!
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </tr>
    </table>    
</div>

{% else %}
{% include "menu.tpl" %}
<div>
Error! You do not have permission to view this page.
</div>
{% endif %}

{% endblock %}