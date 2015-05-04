$(document).ready(function(){
    $(".new_accounts_header").click(function(){

        $("#accountsForm").toggle();
        $("#seeMoreAccounts").toggle();
    });


    $(".maintenance_header").click(function(){

        $("#maintenanceForm").toggle();
        $("#seeMoreCars").toggle();

    });

    $("div.switch > label").click(function() {
        var full_id = $(this).parent().find("input").attr("id");
        full_id = full_id.split("-");
        var id = full_id[full_id.length-1];
        var data = {};

        if (full_id[0] == "toggle") {
            var approved = "true";
            if ($(this).parent().find("input").is(":checked")) {
                approved = "false";
                // if it says it is checked now, that means user was un-checking it.
            }
            data = {
                    "acct_id":id,
                    "approved":approved
                };
        } else if (full_id[0] == "suspended") {
            var suspended = "true";
            if ($(this).parent().find("input").is(":checked")) {
                suspended = "false";
                // if it says it is checked now, that means user was un-checking it.
            }
            data = {
                    "acct_id":id,
                    "suspended":suspended
                };
        } else {
            console.log("Full_id: " + full_id[0]);
            console.log($(this).parent().find("input").attr("id"));
        }
         console.log(data);


         $.ajax({
            url: "/accounts",
            method: "POST",
            contentType: 'application/json;charset=UTF-8',
            dataType: "json",
            data: JSON.stringify(data, null, '\t'),
            success: function(data){console.log(data);}
        });

    });
});