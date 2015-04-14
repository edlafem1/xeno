{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}


<link href="style/profile.css" rel="stylesheet" />

<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
                <div id="pageDescription" class="underline">Profile</div>
    </div>

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
                <td>
                {{firstname}} {{lastname}}
                </td>
                <td></td>
                <td></td>
            </tr>
        </tr>
        <tr>
            
        </tr>
    </table>    
    
    
</div>
{% endblock %}