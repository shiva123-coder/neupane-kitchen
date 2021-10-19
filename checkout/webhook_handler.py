from django.http import HttpResponse


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
        return HttpResponse(
            content=f"Webhook recieved : {event['type']}",
            status=200
            )

    def handle_payment_intent_failed(self, event):
        """handle failed payment intent webhook from stripe"""
        return HttpResponse(
            content=f"Webhook recieved : {event['type']}",
            status=200
            )


            
