var Login = {
    basic: function() {
        var a = $("#login-form").serializeArray();
        $.ajax({
            url: "../server/login.php",
            type: "POST",
            data: a,
            dataType: "html",
            beforeSend: function() {},
            complete: function() {},
            error: function(a, b, c) {
                console.log(c);
            },
            success: function(a, b, c) {
                var d = a.trim();
                if ("success" == d) {
                    window.location = "home.html";
                }
                else {

                    $("#alert").append(" <div class=\"alert alert-danger\" >" +
                        "<a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\"> ×</a>" +
                            "Incorrect Username or Password </div>"
                        );


                }


            }

        });
    }
};


$(document).on('click', '#submitbutton', function() {

    Login.basic();

});