// + and - sign to increase and decrease the quantity once clicked
// + buttton to increase
$('.increase-qty').click(function(e) {
    e.preventDefault();
    var newInput = $(this).closest('.input-group').find('.qty_input');
    var newValue = parseInt($(newInput).val());
    $(newInput).val(newValue + 1);
});

// - button to decrease
$('.decrease-qty').click(function(e) {
    e.preventDefault();
    var newInput = $(this).closest('.input-group').find('.qty_input');
    var newValue = parseInt($(newInput).val());
    $(newInput).val(newValue - 1);
});
