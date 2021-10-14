// javascript logic to set up stripe
// taken from stripe Documentation and modified as per project requirement.

// slice method to remove quotation mark on the key
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
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
