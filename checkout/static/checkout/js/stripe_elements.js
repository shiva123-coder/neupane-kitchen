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

    stripe.confirmCardPayment(clientSecret, {
        payment_method:{
            card: card,
        }
    }).then(function(outcome){
        if (outcome.error){
            let errorMsg = document.getElementById("card-errors");
            let html = `
                <p class="text-danger mt-1">
                <i class="fas fa-exclamation" aria-hidden="true"></i>
                ${outcome.error.message}</p>`;
            errorMsg.innerHTML = html;
            // re-enable card-element and checkout button for user if there is an error
            card.update({"disabled": false});
            $('#checkout-btn').attr('disabled', false);

        } else {
            if (outcome.paymentIntent.status === 'succeeded'){
                form.submit();
            }
        }
    });
});
