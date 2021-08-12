$('#recipeCarousel').carousel({
  interval: 10000
})

$('.carousel .carousel-item').each(function () {
  var minPerSlide = 4;
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(':first');
  }
  next.children(':first-child').clone().appendTo($(this));

  for (var i = 0; i < minPerSlide; i++) {
    next = next.next();
    if (!next.length) {
      next = $(this).siblings(':first');
    }

    next.children(':first-child').clone().appendTo($(this));
  }
});
$(document).ready(function () {
  $("#sCard").hover(function (event) {
    event.preventDefault();
    $("#arrow3").toggle(500);
    $("#Three").css("color", "#ffde22")
  });
  $("#sCard").mouseout(function (event) {
    event.preventDefault();
    $("#Three").removeAttr("style");
  });
});

$(function () {
  $("#typ").typed({
    strings: ["We Got Good Shit!"],
    typeSpeed:200
  });
});