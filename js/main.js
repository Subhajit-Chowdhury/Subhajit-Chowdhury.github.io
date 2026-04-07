$(document).ready(function(){
    $("#landing-chevron").click(function() {
        $('html,body').animate({scrollTop: $("#details-container").offset().top},'slow');
    });
    $("#find-out-text").click(function() {
        $('html,body').animate({scrollTop: $("#details-container").offset().top},'slow');
    });
});

$(window).scroll(function (){
    var opac1 = ($("#heading-name").offset().top - $(window).scrollTop() + 50)/($("#heading-name").offset().top + 50);
    if(opac1<0) opac1 = 0;
    $("#heading-name").css("opacity",opac1);
    $("#heading-title").css("opacity",opac1);
    $("#landing-footer").css("opacity",opac1);


    var aboutTop = $("#about").offset().top;
    var aboutHeight = $("#about").height();
    //console.log(aboutTop+" "+aboutHeight+" "+$(window).scrollTop());
    var opac2 = (aboutTop - $(window).scrollTop() + 1.2*aboutHeight)/(aboutHeight);
    if(opac2>1) opac2 = 1;
    if(opac2<0) opac2 = 0;
    $("#internship-about").css("opacity",opac2);
    $("#internship-nav").css("opacity",1-opac2); 
});





// var intervalId = window.setInterval(function(){
//     currentPosition = $(window).scrollTop();
//     elements = $(".main-content-element");
//     length = elements.length;
//     for(i=0;i<length-1;i++){
//         if((currentPosition < elements[i+1].offsetTop-50)&&(currentPosition > elements[i].offsetTop+50)){
//             threshold = (elements[i+1].offsetTop - elements[i].offsetTop)/3;
//             if(currentPosition > elements[i].offsetTop + threshold){
//                 $('html,body').animate(
//                     {scrollTop: elements[i+1].offsetTop},
//                     {
//                         easing: 'swing',
//                         duration:0,
//                         complete:function(){console.log('hi');}
//                 });
//                 break;
//             }
//         }
//     }
// }, 500);



// var flag = 1;
// var lastScrollTop = 0;
// var intervalId = window.setInterval(function(){
//   flag=1;
// }, 1000);
// $(window).scroll(function () { 
//     if(flag == 1){
//         currentPosition = $(window).scrollTop();
//         elements = $(".main-content-element");
//         length = elements.length;
//         console.log(currentPosition +" "+lastScrollTop); 
//         if(lastScrollTop<currentPosition){
//             //Scrolling Down
//             lastScrollTop = currentPosition;
//             for(i=0;i<length-1;i++){
//                 if((currentPosition < elements[i+1].offsetTop-50)&&(currentPosition > elements[i].offsetTop+50)){
//                     threshold = (elements[i+1].offsetTop - elements[i].offsetTop)/2;
//                     if(currentPosition > elements[i].offsetTop + threshold){
//                         flag = 0;
//                         $('html,body').animate(
//                             {scrollTop: elements[i+1].offsetTop},
//                             {
//                                 easing: 'swing',
//                                 duration:0,
//                                 complete:function(){console.log('hi');}
//                         });
//                         break;
//                     }
//                 }
//             }
//         }else{
//             lastScrollTop = currentPosition;
//             console.log('going up');
//         }
//     }
    
// });