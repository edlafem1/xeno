{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}
<!-- Moved this to dashboard.tpl so all main pages have jQuery
<script src="//code.jquery.com/jquery-1.10.2.js"></script>
<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
-->

<link href="/style/car_profile.css" rel="stylesheet" />
<link href="/style/dash_style.css" rel="stylesheet" />

<div class="fadeInUp">
    
    {% if admin %}
    <div id="adminBtnsWrapper">
        <div class="adminBtnGroup">
            <div class="adminBtnText">Enable/Disable</div>
            <div id="enabled" class="switch floatLeft">
                <input id="toggle-1" class="toggle toggle-round-flat" type="checkbox">
                <label for="toggle-1"></label>
            </div>
        </div>
        
        <div class="adminBtnGroup">
            <div class="adminBtnText">Maintenance</div>
            <div id="maintenance" class="switch floatLeft">
                <input id="toggle-2" class="toggle toggle-round-flat" type="checkbox">
                <label for="toggle-2"></label>
            </div>
        </div>
    </div>
    {% endif %}
    
    
    <div id="pageDescriptionWrapper">
        <div id="pageDescription" class="underline">{{car["year"]|string + " " + car["make"] + " " + car["model"] }}</div>
    </div>

    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <h4 class="message_flash">{{ messages[0] }}</h4>
        {% endif %}
    {% endwith %}

    <div id="carWrapper">
        <img src="/images/cars/{{ car["id"] }}_main.pic" style="display: block; margin: 0px auto; height: 100%;">
    </div>
    
    <div id="pageDescriptionWrapper">
        <div id="pageDescription" class="underline">Performance</div>
    </div>
    
    <div class="performanceList">
        <div class="performanceInfo">
            <div class="softUnderline">Horsepower</div>
            <div class="performanceValue">{{ car["hp"] }}</div>
        </div>
        <div class="performanceInfo">
            <div class="softUnderline">Torque</div>
            <div class="performanceValue">{{ car["torque"] }}</div>
        </div>
        <div class="performanceInfo">
            <div class="softUnderline">0-60</div>
            <div class="performanceValue">{{ car["acceleration"] }} sec</div>
        </div>
        <div class="performanceInfo">
            <div class="softUnderline">Max Speed</div>
            <div class="performanceValue">{{ car["max_speed"] }} MPH</div>
        </div>
        <div class="performanceInfo">
            <div class="softUnderline">Type</div>
            <div class="performanceValue">{{ car["ctype"] }}</div>
        </div>
        <div class="performanceInfo">
            <div class="softUnderline">Country</div>
            <div class="performanceValue">{{ car["country"] }}</div>
        </div>
    </div>
    
    
    
    
    <div id="pageDescriptionWrapper">
        <div id="pageDescription" class="underline">Rent This Car</div>
    </div>
    

    <!-- datepicker.value is the date that they selected -->
    <div class="rentGroup">
        <div onclick="//alert(this.value)" id="datepicker"></div>
    </div>
    
    
    <!-- Reviews Section -->
    <div id="pageDescriptionWrapper">
        <div id="pageDescription" class="underline">Reviews</div>
    </div>
    

    <div class="reviewsList">
        {% for review in reviews %}
        <div class="review">
            <div class="profilePic">
                <img src="/images/profiles/blank_face.jpeg" style="width: 100%; height: 100%;">
            </div>
            <div class="reviewInfo">
                <div class="reviewer">{{ review["fname"] + review["lname"] }}</div>
                <div>
                    {% for count in star_range %}
                        {% if loop.index < review["num_stars"] %}
                            <span class="star on">☆</span>
                        {% else %}
                            <span class="star">☆</span>
                        {% endif %}
                    {% endfor %}
                </div>
                <div class="reviewText">
                    {% autoescape on %}
                    {{ review["text"] }}
                    {% endautoescape %}
                </div>
            </div>
        </div>
        {% endfor %}
        
        <div class="writeReview">
            <div id="writeReviewText" class="softUnderline">Write a review</div>
            <div style="overflow:hidden;">
                <div id="ratingText">Rating:</div>
                <div id="ratingDiv" class="rating">
                    <span id="5" onclick="rating(5)">☆</span>
                    <span id="4" onclick="rating(4)">☆</span>
                    <span id="3" onclick="rating(3)">☆</span>
                    <span id="2" onclick="rating(2)">☆</span>
                    <span id="1" onclick="rating(1)">☆</span>
                </div>
            </div>
            <div class="yourReview">
                <textarea id="newReview"
                          onfocus="checkText(); setbg('white');"
                          onblur="checkText(); setbg('lightgrey')">Favorite detail about this car?
                </textarea>
            </div>
            
            <div id="login_buttom_wrapper">
            <button onclick="submitReview()" class="button button-border-primary button-rounded">Submit</button>
            </div>
        </div>
        
    </div>
    
</div>

<form id="rentalForm" action="/reserve" method="POST" style="display: none;">
    <input id="rentalDate" name="rentalDate" type="text" style="display: none;"/>
    <input name="which_car" type="hidden" value="{{ car['id'] }}"/>
    <input type="submit" style="display: none;"/>
</form>

<form id="reviewForm" action="" method="get" style="display: none;">
    <input id="carRating" type="text" style="display: none;"/>
    <input id="carReview" type="text" style="display: none;"/>
    <input type="submit" style="display: none;"/>
</form>


<script src="/scripts/car_profile.js" type="text/javascript"></script>

{% endblock %}