$(document).ready(function() {
  $("#datepicker").datepicker(); });

// $(document).ready(function(){
//
//   $("#act").click(function(){
//     $('.activities').addClass('active')
//     .animate({
//     opacity: 0.8,
//     left: "+=50",
//     height: "toggle"
//   }, 700, function() {
//     // Animation complete.
//   });
//   $("#act").hide();
//   });
// });

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

$("#goback").click(function() {
  $("html, body").animate({ scrollTop: 0 }, "slow");
  return false;
});
// var $elem = $('body');
// $('#goback').click(
// function (e) {
//   console.log('click')
// $('html, body').animate({scrollTop: $elem.height()}, 1000);
// }
// );
$(function () {
    setNavigation();
});

function setNavigation() {
    var path = window.location.pathname;
    path = path.replace(/\/$/, "");
    path = decodeURIComponent(path);

    $("#main-nav a").each(function () {
        var href = $(this).attr('href');
        if (path.substring(0, href.length) === href) {
            $(this).closest('a').addClass('active');
        }
    });
}
