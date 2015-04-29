{% extends "dashboard.tpl" %}
{% block body %}

{% include "menu.tpl" %}

<script src="//code.jquery.com/jquery-1.10.2.js"></script>
<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>


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
        <div id="pageDescription" class="underline">2015 Ford Focus{{ car["id"] }}</div>
    </div>
    
    <div id="carWrapper">
        <img src="/images/cars/_main.pic" style="display: block; margin: 0px auto; height: 100%;">
    </div>
    
    <div id="pageDescriptionWrapper">
        <div id="pageDescription" class="underline">Performance</div>
    </div>
    
    <div class="performanceList">
        <div class="performanceInfo">
            <div class="softUnderline">Horsepower</div>
            <div class="performanceValue">1,000</div>
        </div>
        <div class="performanceInfo">
            <div class="softUnderline">Torque</div>
            <div class="performanceValue">A lot</div>
        </div>
        <div class="performanceInfo">
            <div class="softUnderline">0-60</div>
            <div class="performanceValue">.5 sec</div>
        </div>
        <div class="performanceInfo">
            <div class="softUnderline">Max Speed</div>
            <div class="performanceValue">374 MPH</div>
        </div>
        <div class="performanceInfo">
            <div class="softUnderline">Type</div>
            <div class="performanceValue">Coupe</div>
        </div>
        <div class="performanceInfo">
            <div class="softUnderline">Country</div>
            <div class="performanceValue">Germany</div>
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
        <div class="review">
            <div class="profilePic">
                <img src="/images/profiles/blank_face.jpeg" style="width: 100%; height: 100%;">
            </div>
            
            <div class="reviewInfo">
                <div class="reviewer">Michael Bishoff</div>
                <div>
                    <span class="star on">☆</span>
                    <span class="star on">☆</span>
                    <span class="star on">☆</span>
                    <span class="star">☆</span>
                    <span class="star">☆</span>
                </div>
                <div class="reviewText">
                    Excellent ride! I really like how it drives. It has wheels, so that's a plus.. or it's a minus if you would rather have flying cars. Yeah.. Now that I think about it, I would rather have a flying car over this car any day. Easily. No questions asked.
                
                </div>
            </div>
        </div>
        
        <div class="review">
            <div class="profilePic">
                <img src="/images/profiles/blank_face.jpeg" style="width: 100%; height: 100%;">
            </div>
            
            <div class="reviewInfo">
                <div class="reviewer">Michael Bishoff</div>
                <div>
                    <span class="star on">☆</span>
                    <span class="star on">☆</span>
                    <span class="star on">☆</span>
                    <span class="star">☆</span>
                    <span class="star">☆</span>
                </div>
                <div class="reviewText">
                    Excellent ride! I really like how it drives. It has wheels, so that's a plus.. or it's a minus if you would rather have flying cars. Yeah.. Now that I think about it, I would rather have a flying car over this car any day. Easily. No questions asked.
                
                </div>
            </div>
        </div>
        
        <div class="review">
            <div class="profilePic">
                <img src="/images/profiles/blank_face.jpeg" style="width: 100%; height: 100%;">
            </div>
            
            <div class="reviewInfo">
                <div class="reviewer">Michael Bishoff</div>
                <div>
                    <span class="star on">☆</span>
                    <span class="star on">☆</span>
                    <span class="star on">☆</span>
                    <span class="star">☆</span>
                    <span class="star">☆</span>
                </div>
                <div class="reviewText">
                    Excellent ride! I really like how it drives. It has wheels, so that's a plus.. or it's a minus if you would rather have flying cars. Yeah.. Now that I think about it, I would rather have a flying car over this car any day. Easily. No questions asked.
                
                </div>
            </div>
        </div>
        
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

<form id="rentalForm" action="" method="get" style="display: none;">
    <input id="rentalDate" type="text" style="display: none;"/>
    <input type="submit" style="display: none;"/>
</form>

<form id="reviewForm" action="" method="get" style="display: none;">
    <input id="carRating" type="text" style="display: none;"/>
    <input id="carReview" type="text" style="display: none;"/>
    <input type="submit" style="display: none;"/>
</form>


<script src="/scripts/car_profile.js" type="text/javascript"></script>

{% endblock %}