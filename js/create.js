function generate() {
    $(document).ready(function() {

        var a = $("#create-table-form").serializeArray();
        $.ajax({
            url: "../server/create.php",
            type: "POST",
            data: a,
            //dataType: "html",
            beforeSend: function() {},
            complete: function() {},
            error: function(a, b, c) {
                console.log(c);
            },
            success: function(a, b, d) {

                localStorage.setItem("timetable", a);

                window.location = "status.html";


            }

        });
    });
}


$(document).on('click', '#submitbutton', function() {

    generate();

});