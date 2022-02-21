
// + and - sign to increase and decrease the quantity once clicked
// + buttton to increase the quantity
$('.increase-qty').click(function(e) {
    e.preventDefault();
    var newInput = $(this).closest('.input-group').find('.qty_input');
    var newValue = parseInt($(newInput).val());
// + button disable once input value reach 50
    if( newValue > 3 ){
        $('increase-qty').disabled = true;
        }
    else {
        $(newInput).val(newValue + 1);
    }
});

// - button to decrease the input quantity
$('.decrease-qty').click(function(e) {
    e.preventDefault();
    var newInput = $(this).closest('.input-group').find('.qty_input');
    var newValue = parseInt($(newInput).val());
// + button disable to restric user from iputting the quantity less than 1
    if( newValue < 2 ){
        $('decrease-qty').disabled = true;
        }
    else {
        $(newInput).val(newValue - 1);
    }
});

//scroll icon
// scroll icon only visible once screen is scroll down to over 100px
$(window).scroll(function(){
    var screenHeight = $(window).scrollTop();
    if (screenHeight > 100) {
        $('#scroll-icon').fadeIn();
    } else {
        $('#scroll-icon').fadeOut(2000);
    }
});

// once click on scroll icon, page scroll back to the top
$('#scroll-icon').click(function(e){
    window.scrollTo(0,0)
});

// //  Diasble mouse right click and cut, copy and paste from web content
// $(document).ready(function () { 
//     // Disable mouse click
//     //Disable full page 
//     $("body").on("contextmenu",function(e){ 
//         return false; 
//     }); 
     
//     //Disable part of page 
//     $("#id").on("contextmenu",function(e){ 
//         return false; 
//     }); 

//     // Disable Cut Copy & Paste
//      //Disable full page 
//      $('body').bind('cut copy paste', function (e) { 
//         e.preventDefault(); 
//     }); 
     
//     //Disable part of page 
//     $('#id').bind('cut copy paste', function (e) { 
//         e.preventDefault(); 
//     }); 

//     // Disable Mouse Right Click, Cut, Copy & Paste
//      //Disable cut copy paste 
//      $('body').bind('cut copy paste', function (e) { 
//         e.preventDefault(); 
//     }); 
    
//     //Disable mouse right click 
//     $("body").on("contextmenu",function(e){ 
//         return false; 
//     }); 
// }); 


$('.card-pay-option').hide();
$('.cash-pay-option').hide();

$('.btn-payment').click(function(){
    $('.btn-payment').hide();
    $('.card-pay-option').show();
    $('.cash-pay-option').show();
});



