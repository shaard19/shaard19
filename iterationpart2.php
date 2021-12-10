<?php
$str = "Apple is healthy.";
$delimiter = ' ';
$words = explode($delimiter, $str);
 
foreach ($words as $word) {
    echo $word;
    echo "<br>";
}
?>