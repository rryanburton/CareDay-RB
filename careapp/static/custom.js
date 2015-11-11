$(document).ready(function() {
  $("#datepicker").datepicker(); });

$(document).ready(function(){
  // $("#activity-moods").click(function(){
  //   $('#activity-moods').load('dailyreport/update/');
  //      return false;
  //   });
  //   $('#report1').click(function () {
  //    $('#report1').load('/diapering/new');
  //       return false;
  //    });
  // $("#report2").click(function(){
  //    $('#report2').load('/sleeping/new');
  //       return false;
  //    });
  // $("#report3").click(function(){
  //   $('#report3').load('/eating/new');
  //      return false;
  //   });
  $("#diaper").on('click', function(){
      $("#diaper").addClass('active');
      
  });


});
