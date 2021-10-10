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


// update and remove option in the basket after quantity modification
// update quantity
$('.update-qty').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})
// remove quantity
$('.remove-qty').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_');
    var url = `/basket/remove/${itemId}`;
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
     .done(function() {
         location.reload();
     });
})