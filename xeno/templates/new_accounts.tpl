{% extends "dashboard.tpl" %}
{% block body %}

{% if admin %}
{% include "menu.tpl" %}

<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
        <div id="pageDescription" class="underline">Newly Registered Accounts</div>
    </div>

    <table id="accountsTable" cellspacing=25 class="fadeInUp">
        {% for i in range( accounts | length) %}
        
            <tr class="underline">
                <td>{{ accounts[i]['name'] }}</td>
                <td>{{ accounts[i]['address'] }}</td>
                <td>{{ accounts[i]['paid'] }}</td>
                <td>{{ accounts[i]['approved'] }}</td>
                <td>
                    <div class="switch">
                        <input id="toggle-{{ i }}" class="toggle toggle-round-flat" type="checkbox">
                        <label for="toggle-{{ i }}"></label>
                    </div>
                </td>
            </tr>
        {% endfor %}
    </table>
</div>

{% else %}
{% include "menu.tpl" %}
<div>
Error! You do not have permission to view this page.
</div>
{% endif %}

{% endblock %}