from django.http import HttpResponse

from profiles.models import UserProfile
from .models import Order, OrderLineItem
from menu.models import Item

import json
import time


class StripeWebhookHandler:
    """stripe webhook handler"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """handle unknown webhook event"""
        return HttpResponse(
            content=f"Unhandled webhook recieved : {event['type']}",
            status=200
            )

    def handle_payment_intent_succeeded(self, event):
        """handle succedeed payment intent webhook from stripe"""
        intent = event.data.object
        payment_intent_id = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        sum_total = round(intent.charges.data[0].amount/100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1

        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    contact_number__iexact=shipping_details.phone,
                    street_address__iexact=shipping_details.address.line1,
                    postal_code__iexact=shipping_details.address.postal_code,
                    sum_total=sum_total,
                    original_basket=basket,
                    stripe_payment_intent_id=payment_intent_id,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name=shipping_details.name,
                        phone_number=shipping_details.phone,
                        street_address=shipping_details.address.line1,
                        postal_code=shipping_details.address.postal_code,
                        original_basket=basket,
                        stripe_payment_intent_id=payment_intent_id,
                    )
                for item_id, quantity in json.loads(basket).items():
                    item = Item.objects.get(id=item_id)
                    # cretes the line items
                    order_line_item = OrderLineItem(
                        order=order, item=item,
                        quantity=quantity,
                        )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content="Webhook recieved \
                    : {event['type']} | ERROR : {e}", status=500)
        return HttpResponse(
            content=f"Webhook recieved : {event['type']} | \
                SUCCESS: Created order in webhook", status=200)

    def handle_payment_intent_failed(self, event):
        """handle failed payment intent webhook from stripe"""
        return HttpResponse(
            content=f"Webhook recieved : {event['type']}",
            status=200
            )
        
