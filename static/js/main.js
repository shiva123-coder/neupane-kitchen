
// + and - sign to increase and decrease the quantity once clicked
// + buttton to increase the quantity
$('.increase-qty').click(function(e) {
    e.preventDefault();
    var newInput = $(this).closest('.input-group').find('.qty_input');
    var newValue = parseInt($(newInput).val());
// + button disable once input value reach 50
    if( newValue > 49 ){
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
