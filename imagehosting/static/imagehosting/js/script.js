$(window).load(function() {
  resizer();
  $('.spinner').fadeOut();
  $('#page-preloader').delay(350).fadeOut('slow');
})

$(window).resize(function() {
  resizer();
})

function resizer() {
  var imgs = $('img');
  var row_width = $(window).width() - 50;
  var prev = [];
  var total_w = 0;
  imgs.each(function (i, e) {
    $(this).height(200);
    prev[prev.length] = $(e);
    total_w += $(e).width();
    if (total_w > row_width) {
      prev = $(prev);
      prev.each(function (indx, element) {
        $(element).height(row_width*200/total_w);
      });
      prev = [];
      total_w = 0;
    }
  })
}
