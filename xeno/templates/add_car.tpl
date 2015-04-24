{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}

<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
                <div id="pageDescription" class="underline">Add New Car</div>
    </div>
    <form action="{{ url_for('add_car') or 'add_car' }}" method="POST" autocomplete="off">
    <table cellspacing=25 class="fadeInUp">
        <tr>
            <td>Make:</td>
            <td><input type="text" name="make" placeholder="Ex: Toyota"/></td>
        </tr>
        <tr>
            <td>Model:</td>
            <td><input type="text" name="model" placeholder="Ex: Corolla"/></td>
        </tr>
        <tr>
            <td>Year:</td>
            <td><input type="text" name="year" placeholder="Ex: 2013"/></td>
        </tr>
        <tr>
            <td>Country:</td>
            <td><input type="text" name="country" placeholder="Ex: Italy"/></td>
        </tr>
        <tr>
            <td>Car Type:</td>
            <td><input type="text" name="ctype" placeholder="Ex: Sedan"/></td>
        </tr>
        <tr>
            <td>Odometer:</td>
            <td><input type="text" name="odo" placeholder="Ex: 20000(in miles)"/></td>
        </tr>
        <tr>
            <td>Horsepower:</td>
            <td><input type="text" name="hp" placeholder="Ex: 132"/></td>
        </tr>
        <tr>
            <td>Torque:</td>
            <td><input type="text" name="torque" placeholder="Ex: 128"/></td>
        </tr>
        <tr>
            <td>Acceleration:</td>
            <td><input type="text" name="acceleration" placeholder="Ex: 10(seconds for 0-60mph)"/></td>
        </tr>
        <tr>
            <td>Max Speed:</td>
            <td><input type="text" name="max_speed" placeholder="Ex: 220(in mph)"/></td>
        </tr>
        <tr>
            <td>Featured:</td>
            <td><input type="checkbox" name="is_featured"></td>
        </tr>
        <!--
        <tr>
            <td>Engine:</td>
            <td><input type="text" placeholder="Ex: V4"/></td>
        </tr>
        -->
    </table>

    <div id="add_car_submit_wrapper">
        <button class="button button-border-primary button-rounded">Submit</button>
    </div>
    </form>
</div>
{% endblock %}