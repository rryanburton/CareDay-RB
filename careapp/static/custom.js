$(document).ready(function() {
  $("#datepicker").datepicker(); });

$(document).ready(function(){
  $("#report1").click(function(){
    //make a request
    $.ajax({
            url: "/diapering/new",
            cache: false
        }).done(function (html) {
            $("#report1").append(html);
            $("#report1").show("slow");
        });
  });
  $("#report2").click(function(){
    //make a request
    $.ajax({
            url: "/sleeping/new",
            cache: false
        }).done(function (html) {
            $("#report2").append(html);
            $("#report2").show("slow");
        });
  });
  $("#report3").click(function(){
    //make a request
    $.ajax({
            url: "/eating/new",
            cache: false
        }).done(function (html) {
            $("#report3").append(html);
            $("#report3").show("slow");
        });
  });
});

// jQuery(function() {
//     var form = jQuery("#diaper");
//     form.submit(function(e) {
//         jQuery("#sendbutton").attr('disabled', true)
//         jQuery("#sendwrapper").prepend('<span>Sending message, please wait... </span>')
//         jQuery("#report1").load(
//             form.attr('action') + ' #report1',
//             form.serializeArray(),
//             function(responseText, responseStatus) {
//                 jQuery("#save_child").attr('disabled', false)
//             }
//         );
//         e.preventDefault();
//     });
// });
