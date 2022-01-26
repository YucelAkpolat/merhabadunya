$(document).ready(function(){
    $('.owl-carousel').owlCarousel({
        loop:true,
        margin:20,
        
        center:true,
        autoplay:true,
        autoplayTimeout:3000,
         autoplayHoverPause:false,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            900:{
                items:3
            },
            1000:{
                items:3
            }
        }
    })
    
  });


 
  
  $('.remove').click(function(){
    $('.bottom').removeClass("clicked");
  });


  $('.option').click(function(){
    $('.option').removeClass('active');
    $(this).addClass('active');
 })

 


$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.yukarikaydir').fadeIn();
        } else {
            $('.yukarikaydir').fadeOut();
        }
    });

    $('.yukarikaydir').click(function () {
        $("html, body").animate({
            scrollTop: 0
        }, 600);
        return false;
    });
});
