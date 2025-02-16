(function ($) {
    "use strict";
    Fancybox.bind('[data-fancybox]', {
        // Your custom options
    });    
    var swiper_photo = new Swiper("#swiper-photos", { 
        slidesPerView: 3,            // Show 3 slides at once
        spaceBetween: 40,            // Spacing between slides
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,        // Keep the active slide centered
        loop: true,
        coverflowEffect: {
            rotate: 0,
            stretch: 0,
            depth: 120,
            modifier: 1,
            slideShadows: false,
        },
        breakpoints: {
            "0": {
                spaceBetween: -100,
                slidesPerView: 2
            },
            "575": {
                spaceBetween: 30,
                slidesPerView: 2
            },

            "1199": {
                spaceBetween: 30,
                slidesPerView: 3
            }
        }
    });


})(jQuery);