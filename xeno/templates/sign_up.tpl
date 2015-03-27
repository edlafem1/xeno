{% extends "index.tpl" %}
{% block body %}
<div class="container">
    <h2>Sign Up</h2>
    <br />
    <input type="text" placeholder="Name" />
    <br />
    <br />
    <input type="password" placeholder="Password" />
    <br />
    <br />
    <input type="password" placeholder="Re-Enter Password" />
    <br />
    <br />
    <input type="text" placeholder="Email" />
    <br />
    
</div>
{% endblock %}
<!--
<div class="container">
    <h2>View 1</h2>
    Name:
    <br />
    <input type="text" data-ng-model="filter.name" /> {{ filter.name }}
    <br />
    <ul>
        <li data-ng-repeat="cust in customers | filter:filter.name | orderBy:'name'">{{ cust.name | uppercase }} - {{ cust.city }}</li>
    </ul>
    
    <br />
    Customer Name:<br />
    <input type="text" data-ng-model="newCustomer.name" />
    <br />
    Customer City:<br />
    <input type="text" data-ng-model="newCustomer.city" />
    <br />
    <button data-ng-click="addCustomer()">Add Customer</button>
    <br /><br />
    <a href="#view2">View 2</a>
    
</div>
-->