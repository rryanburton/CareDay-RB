// $(document).ready(function() {
//   $("#datepicker").datepicker(); });

// you can click on the h1 welcome message on landing page and it will take you
// to our contact info

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


// make links active when clicked

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
$(function() {
    $("#archive-date").pagination('selectPage', pageNumber);
});
