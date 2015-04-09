{% extends "dashboard.tpl" %}
{% block body %}

{% if admin %}
{% include "admin_menu.tpl" %}
{% else %}
{% include "menu.tpl" %}
{% endif %}

<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
                <div id="pageDescription" class="underline">Add New Car</div>
    </div>

    <table cellspacing=25 class="fadeInUp">
        <tr>
            <td>Make:</td>
            <td><input type="text" placeholder="Ex: Toyota"/></td>
        </tr>
        <tr>
            <td>Model:</td>
            <td><input type="text" placeholder="Ex: Corolla"/></td>
        </tr>
        <tr>
            <td>Year:</td>
            <td><input type="text" placeholder="Ex: 2013"/></td>
        </tr>
        <tr>
            <td>License Plate:</td>
            <td><input type="text" placeholder="Ex: T00F4S7"/></td>
        </tr>
        <tr>
            <td>Horsepower:</td>
            <td><input type="text" placeholder="Ex: 132"/></td>
        </tr>
        <tr>
            <td>Torque:</td>
            <td><input type="text" placeholder="Ex: 128"/></td>
        </tr>
        <tr>
            <td>Engine:</td>
            <td><input type="text" placeholder="Ex: V4"/></td>
        </tr>
    </table>
    
    <div id="add_car_submit_wrapper">
        <div class="button button-border-primary button-rounded">Submit</div>
    </div>
</div>
{% endblock %}