<!DOCTYPE html>
<html>
<head>
<title>Create Percentage Calculator Using JavaScript</title>
</head>
<body>
<h2>Create Percentage Calculator Using JavaScript</h2>
Marks Possible Number:<br>
<input type="text" id="pointspossible"/>
<br>
Given Marks Number:<br>
<input type="text" id="pointsgiven"/>
<br>
Percentage:<br>
<input type="text" id="pointsperc" disabled/>
<br>
</body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(function(){
$('#pointspossible').on('input', function() {
calculate();
});
$('#pointsgiven').on('input', function() {
calculate();
});
function calculate(){
var Possible = parseInt($('#pointspossible').val()); 
var pgiven = parseInt($('#pointsgiven').val());
var perc="";
if(isNaN(Possible) || isNaN(pgiven)){
perc=" ";
}else{
perc = ((pgiven/Possible) * 100).toFixed(3);
}
$('#pointsperc').val(perc);
}
});
</script>
</html>