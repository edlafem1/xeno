/*
    Checks if the textbox is about to be written to and removes the 
    placeholder text if so. Keeps the user's text if it's there.
    Puts back the placeholder if the user leaves it blank.
*/
function checkText() {
    var textarea = document.getElementById("newReview");

    if (textarea.value == textarea.defaultValue){
        textarea.value = '';
    }
    else if (textarea.value.replace(/\s/g,'') == ''){
        textarea.value = textarea.defaultValue;
    }
}

/* Sets the background color of the textarea */
function setbg(color) {
    document.getElementById("newReview").style.background=color
}

function rating(score) {
    $("#carRating").val(score);

    // Removes the dynamic star behavior
    $( "#ratingDiv" ).removeClass( "rating" );

    // Adds the static star behavior
    for (var i = 1; i < 6; i++){
        $("#" + (i)).addClass("star");
    }
    // Turn on the left most stars
    for (var i = score; i > 0; i--){
        $("#" + (6-i)).addClass("on");
    }

    // Set the group to remove the static behavior and enable the 
    // dynamic behavior when the mouse enters the div again
    $( "#ratingDiv" ).on( "mouseenter", function() {
        $("#ratingDiv").addClass("rating");
        $("#carRating").val(0);

        for (var i = 1; i < 6; i++){
            $("#" + (i)).removeClass("star on");
        }
    });
}

function submitReview() {

    $("#carReview").val($("#newReview").val());
    //alert($("#carRating").val() + " : " + $("#carReview").val());
    $("#carRating").val($("#carRating").val());
    $("#carReview").val($("#carReview").val());
    /* Why ^^ ?? - Bishoff is asking */
    
    $("#reviewForm").submit();
}

/* JQuery vv    Not JQuery ^^     Why not */


// Creates the datepicker



function unavailable(date) {
    dmy = date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear();
    if ($.inArray(dmy, unavailableDates) == -1) {
        return [true, ""];
    } else {
        return [false, "", "Unavailable"];
    }
}

/*
$(function() {
    $( "#datepicker" ).datepicker();
});
*/
// When the user selects a date, submit the date
$('#datepicker').datepicker({
    onSelect: function(dateText, inst){
        // Assigns the date to the hidden form
        $("#rentalDate").val($(this).val());

        var date = $("#rentalDate").val();
        //console.log($("#rentalDate").val());
        // Submits the form
        $( "#rentalForm" ).submit();
    },
     beforeShowDay: unavailable,
     minDate: new Date()
});
