$(document).ready(function(){
    $(".new_accounts_header").click(function(){

        $("#accountsForm").toggle();
        $("#seeMoreAccounts").toggle();

        $.ajax({
            url: "/ajax_test",
            method: "GET",
            contentType: 'application/json;charset=UTF-8',
            dataType: "json",
            data: {
                "var1":4,
                "var2":5,
                "var3":"hello"
                },
            success: function(data){console.log(data);}
        });

    });


    $(".maintenance_header").click(function(){

        $("#maintenanceForm").toggle();
        $("#seeMoreCars").toggle();

    });
});