{% extends "dashboard.tpl" %}
{% block body %}

{% if admin %}
{% include "menu.tpl" %}

<div class="fadeInUp">
    <div id="pageDescriptionWrapper">
        <div id="pageDescription" class="underline">Newly Registered Accounts</div>
    </div>

    <form id="accountsForm" action="" method="GET">
        <table id="accountsTable" cellspacing=25 class="fadeInUp">
            {% for i in range( accounts | length) %}

                <tr class="underline">
                    <td>{{ accounts[i]['name'] }}</td>
                    <td>{{ accounts[i]['address'] }}</td>
                    <td>{% if accounts[i]['paid'] %}
                            Paid
                        {% else %}
                            NOT PAID
                        {% endif %}
                    </td>
                    <td>{% if accounts[i]['approved'] %}
                        Approved
                        {% else %}
                        NOT APPROVED
                        {% endif %}
                    </td>
                    <td>
                        <div class="switch">
                            <input id="toggle-{{ i }}" class="toggle toggle-round-flat" type="checkbox" 
                                  {% if accounts[i]['approved'] %}
                                   checked
                                    {% endif %}

                                   >
                            <label for="toggle-{{ i }}"></label>
                        </div>
                    </td>
                </tr>
            {% endfor %}
            <tr>
                <td colspan="5"><div id="login_buttom_wrapper">
                    <button class="button button-border-primary button-rounded">Submit Changes</button>
        </div></td>
            </tr>
        </table>
    </form>
</div>

{% else %}
{% include "menu.tpl" %}
<div>
Error! You do not have permission to view this page.
</div>
{% endif %}

{% endblock %}