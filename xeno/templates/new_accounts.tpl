{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}
<script type="text/javascript" src="/scripts/account.js"></script>
<style type="text/css">
    .new_accounts_header:hover, .maintenance_header {
        cursor: pointer;
    }

    #seeMoreAccounts, #seeMoreCars {
        text-align: center;
        display: none;
        margin-bottom: 3em;
    }

</style>

<div class="fadeInUp">
    <div id="pageDescriptionWrapper" class="new_accounts_header">
        <div id="pageDescription" class="underline"><span>Newly Registered Accounts</span></div>
    </div>

    {% if accounts | length > 0 %}
    <form id="accountsForm" action="" method="GET">
        <table id="accountsTable" cellspacing=25 class="fadeInUp" style="font-size: .7em;">
            <tr class="underline">
                <td>Name</td>
                <td>Email</td>
                <td>Approved</td>
                <td>Suspended</td>
                <td>Account Type</td>
            </tr>
            {% for i in range( accounts | length) %}

                <tr class="underline">
                    <td>{{ accounts[i]['name'] }}</td>
                    <td>{{ accounts[i]['userid'] }}</td>
                    <td>
                        <div class="switch">
                            <input id="toggle-acct-{{ accounts[i]['id'] }}" class="toggle toggle-round-flat" type="checkbox"
                                  {% if not accounts[i]['banned'] %}
                                   checked
                                    {% endif %}
                                   >
                            <label for="toggle-acct-{{ accounts[i]['id'] }}"></label>
                        </div>
                    </td>
                    <td>
                        <div class="switch">
                            <input id="suspended-acct-{{ accounts[i]['id'] }}" class="toggle toggle-round-flat" type="checkbox"
                                   {% if accounts[i]['suspended'] %}
                                    checked
                                    {% endif %}
                                    {% if accounts[i]['banned'] %}
                                    disabled
                                    {% endif %}
                                   >
                            <label for="suspended-acct-{{ accounts[i]['id'] }}"></label>
                        </div>
                    </td>
                    <td>
                        <select id="account_type-{{ accounts[i]['id'] }}">
                            <option value="3"
        {% if accounts[i]['acct_type'] == 3 %}selected="selected"{% endif %}
                                    >User</option>
                            <option value="2"
        {% if accounts[i]['acct_type'] == 2 %}selected="selected"{% endif %}
                                    >Maintenance</option>
                            <option value="1"
        {% if accounts[i]['acct_type'] == 1 %}selected="selected"{% endif %}
                                    >Administrator</option>
                        </select>
                    </td>
                </tr>
            {% endfor %}
            <tr>
                <table id="buttonTable" cellspacing=0 class="fadeInUp" style="font-size: .7em;">
                    <td><td><td><td><td></td></td></td></td></td>
                    <tr>
                    <td colspan="5">
<!--
                        <div id="submit_changes_buttom_wrapper">
                            <button class="button button-border-primary button-rounded">Submit Changes</button>
                        </div>
-->
                    </td>
                    </tr>
                </table>
            </tr>
        </table>
    </form>
<br/>
    <div id="seeMoreAccounts" class="new_accounts_header" style="">See Accounts</div>
    {% endif %}
    
    
    <div id="pageDescriptionWrapper" class="maintenance_header">
        <div id="pageDescription" class="underline">Car Maintenance Log</div>
    </div>

    {% if carMaintenance | length > 0 %}
    <form id="maintenanceForm" action="" method="GET">
        <table id="accountsTable" cellspacing=25 class="fadeInUp">
            {% for car in carMaintenance: %}

                <tr class="underline">
                    <td>{{car["year"]|string + " " + car["make"] + " " + car["model"] }}</td>
                    <td>{{ car['issue'] }}</td>
                    <td>{{ car['miles'] }} Miles</td>
                    {% if True %}
                        <td>
                            Needs Maintenance
                        </td>
                        <td>
                            <div class="switch">
                                <input id="toggle-maint-{{ i }}" class="toggle toggle-round-flat" type="checkbox">
                                <label for="toggle-maint-{{ i }}"></label>
                            </div>
                        </td>
                    {% else %}
                        <td colspan="2">
                            Fixed
                        </td>
                    {% endif %}
                </tr>
            {% endfor %}
            <tr>
                <td colspan="5">
                    <div id="submit_changes_buttom_wrapper">
                        <button class="button button-border-primary button-rounded">Submit Changes</button>
                    </div>
                </td>
            </tr>
        </table>
    </form>
    <div id="seeMoreCars" class="maintenance_header">See Maintenance Log</div>
    {% endif %}
    
    
</div>

{% endblock %}