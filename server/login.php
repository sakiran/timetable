<?php

header("Access-Control-Allow-Origin: *");

session_start();
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $username = $_POST['username'];
    
    $password = $_POST['password'];
    
    if (($username == "keerthana") && ($password == "keerthana123")) {
        
        echo "success";
        
    }
    
}




else {
    echo "login failed";
}

?>