$(document).ready(function(){
  $('.slider').slick({
    arrows: false,
    dots: false,
//    prevArrow: "<img src='static/homepage/img/leftarrow_121320.svg' class='slick-prev' alt='1'>",
//    nextArrow: "<img src='static/homepage/img/rightarrow_121279.svg' class='slick-next' alt='2'>",
    // slidesToShow: 3,
    slidesToScroll: 5,
    speed: 1000,
    infinite: true,
    initialSlide: 0,
    autoplay: true,
    autoplaySpeed: 3000,
    pauseOnFocus: true,
    pauseOnHover: true,
    pauseOnDotsHover: true,
    waitForAnimate: true,
    variableWidth: true,
    responsive:[
      {
        breakpoint: 420,
        settings: {
//          variableWidth: false,
//          slidesToShow: 1,
          slidesToScroll: 1
        }
      }, {
        breakpoint: 770,
        settings: {
          slidesToScroll: 2
        }
      }
    ]
  });
})


$(document).ready(function(){
  $('.slider_small').slick({
    arrows: true,
    prevArrow: `<img src=${pathToPrevImage} class='slick-prev' alt='1'>`,
    nextArrow: `<img src=${pathToNextImage} class='slick-next' alt='2'>`,
    dots: false,
    slidesToShow: 1,
    slidesToScroll: 1,
    speed: 1000,
    infinite: true,
    initialSlide: 0,
    autoplay: false,
    autoplaySpeed: 3000,
    pauseOnFocus: true,
    pauseOnHover: true,
    pauseOnDotsHover: true,
    waitForAnimate: true,
    variableWidth: false,
  });

})




