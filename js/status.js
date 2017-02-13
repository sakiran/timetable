$(document).ready(function() {

                    $("#tabletr").empty();

                    a = localStorage.getItem("timetable");
                    var json = jQuery.parseJSON(a);



                    for (var i = 0; i < json.length; i++) {


                        var subarray = json[i];



                        $("#statustable > tbody").append("<tr>");

                        for (var j = 0; j < subarray.length; j++) {



                            var temp = subarray[j];

                            console.log(temp);

                            if (/^[A-Z]/.test(temp))


                            {
                                $("#statustable > tbody").append("<td class = 'tutorial'>" + subarray[j] + "</td>");
                            } else if (/lab/.test(temp))

                            {
                                $("#statustable > tbody").append("<td class = 'lab'>" + subarray[j] + "</td>");
                            } else

                            {
                                $("#statustable > tbody").append("<td class = 'subject'>" + subarray[j] + "</td>");
                            }




                        }
                        $("#statustable > tbody").append("</tr>");

                    }


                 });