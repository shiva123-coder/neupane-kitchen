// javascript logic to set up stripe
// taken from stripe Documentation and modified as per project requirement.

// slice method to remove quotation mark on the key
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontSize: '14px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle validation errors on card element
card.addEventListener('change', (event) => {
    let errorMsg = document.getElementById("card-errors");
    if (event.error) {
        let html = `
            <p class="text-danger mt-1">
            <i class="fas fa-exclamation" aria-hidden="true"></i>
            ${event.error.message}</p>`;
            errorMsg.innerHTML = html;
    } else {
        errorMsg.textContent = "";
    }
});

// Handle form submission
let form = document.getElementById('checkout-form');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    // disable card element and submit button to prevent multiple submissions
    card.update({"disabled": true});
    $('#checkout-btn').attr('disabled', true);
    $('#checkout-form').fadeToggle();
    $('.loading-overlay').fadeToggle();


    let btnSave = document.getElementById('save-info');
    let saveInfo = false;
    if (btnSave){
        saveInfo = Boolean($('btnSave').attr('checked'))
    }
    // let saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function(){
        stripe.confirmCardPayment(clientSecret, {
            payment_method:{
                card: card,
                billing_details: {
                    name: form.full_name.value.trim(),
                    phone: form.contact_number.value.trim(),
                    email: form.email.value.trim(),
                    full_address: {
                        address: form.address.value.trim(),
                        door_no: form.door_no.value.trim(),
                        postcode: form.postcode.value.trim(),
                        town_or_city: form.town_or_city.value.trim(),
                    }
                }
            },
            delivery_details: {
                name: form.full_name.value.trim(),
                phone: form.contact_number.value.trim(),
                email: form.email.value.trim(),
                full_address: {
                    address: form.address.value.trim(),
                    door_no: form.door_no.value.trim(),
                    postcode: form.postcode.value.trim(),
                    town_or_city: form.town_or_city.value.trim(),
                }
            },
        }).then(function(outcome){
            if (outcome.error){
                let errorMsg = document.getElementById("card-errors");
                let html = `
                    <p class="text-danger mt-1">
                    <i class="fas fa-exclamation" aria-hidden="true"></i>
                    ${outcome.error.message}</p>`;
                errorMsg.innerHTML = html;
                $('#checkout-form').fadeToggle();
                $('.loading-overlay').fadeToggle();
                // re-enable card-element and checkout button for user if there is an error
                card.update({"disabled": false});
                $('#checkout-btn').attr('disabled', false);
    
            } else {
                if (outcome.paymentIntent.status === 'succeeded'){
                    form.submit();
                }
            }
        });
    }).fail(function(){
        // reload the page
        location.reload();
    })
});