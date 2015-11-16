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
$('.scroll').click(
		function (e) {
  $('html, body').animate({scrollTop: $elem.height()}, 1000);
		}
	);
});
$(function() {

        var $elem = $('body');
$('.scroll').click(
		function (e) {
  $('html, body').animate({scrollTop: $elem.height()}, 1000);
		}
	);
});

// dropdown nav function

$('ul.nav li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});
