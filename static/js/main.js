
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

