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
        delivery_details = intent.shipping
        sum_total = round(intent.charges.data[0].amount/100, 2)

        for field, value in delivery_details.address.items():
            if value == "":
                delivery_details.address[field] = None

        order_exists = False
        attempt = 1
        # print("ps-1")
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=delivery_details.name,
                    email__iexact=billing_details.email,
                    contact_number__iexact=delivery_details.phone,
                    street_address__iexact=delivery_details.address.line1,
                    postal_code__iexact=delivery_details.address.postal_code,
                    sum_total=sum_total,
                    original_basket=basket,
                    stripe_payment_intent_id=payment_intent_id,
                )

                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        # print("ps-2")
        if order_exists:
            # print("ps-3")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        else:
            # print("ps-4")
            order = None
            try:
                # print("ps-5")
                order = Order.objects.create(
                        full_name=delivery_details.name,
                        contact_number=delivery_details.phone,
                        email=billing_details.email,
                        street_address=delivery_details.address.line1,
                        postal_code=delivery_details.address.postal_code,
                        original_basket=basket,
                        stripe_payment_intent_id=payment_intent_id,
                    )
                # print("ps5.1")
                for item_id, quantity in json.loads(basket).items():
                    # print("ps5.2")
                    item = Item.objects.get(id=item_id)
                    # print("ps5.3")
                    # cretes the line items
                    order_line_item = OrderLineItem(
                        order=order, item=item,
                        quantity=quantity,
                        )
                    # print("ps5.4")
                    order_line_item.save()
                    # print("ps5.5")
            except Exception as e:
                # print("ps-6")
                if order:
                    order.delete()
                return HttpResponse(content="Webhook recieved \
                    : {event['type']} | ERROR : {e}", status=500)
        # print("ps-7")
        return HttpResponse(
            content=f"Webhook recieved : {event['type']} | \
                SUCCESS: Created order in webhook", status=200)

    def handle_payment_intent_failed(self, event):
        """handle failed payment intent webhook from stripe"""
        return HttpResponse(
            content=f"Webhook recieved : {event['type']}",
            status=200
            )
        
