// update link to allow users to update the qunatity once clicket
$('.update-qty').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})

$('.remove-qty').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/basket/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
     .done(function() {
         location.reload();
     });
})