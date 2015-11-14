$(document).ready(function() {
  $("#datepicker").datepicker(); });

$(document).ready(function(){

  $("#act").click(function(){
    $('.activities').addClass('active')
    .animate({
    opacity: 0.8,
    left: "+=50",
    height: "toggle"
  }, 700, function() {
    // Animation complete.
  });
  $("#act").hide();
  });
});

$(function() {
	// the element inside of which we want to scroll
        var $elem = $('body');
$('#main-nav').click(
		function (e) {
  $('html, body').animate({scrollTop: $elem.height()}, 2000);
		}
	);
});
