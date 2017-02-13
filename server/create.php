<?php 

header("Access-Control-Allow-Origin: *");
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $labs =  $_POST['labs'];
    $tutorial = $_POST['tutorial'];
    $subjects = $_POST['subjects'];
    $code = "python run.py -l ";
    $tute = " -t ";
    $sub = " -s ";

$command = $code.$labs.$tute.$tutorial.$sub.$subjects ;
#echo $command;
$output = shell_exec($command);

$output = str_replace('\'','"',$output);


echo $output;
#$toppings = json_decode($output);


#echo $toppings[1][2];


}


