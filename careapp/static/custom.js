$(document).ready(function() {
  $("#datepicker").datepicker(); });

$(document).ready(function(){
  $("#report1").click(function(){
    //make a request
    $("#report1").load("/diapering/new");

  });
  $("#report2").click(function(){
    //make a request
    $("#report2").load("/sleeping/new");

  });
});
