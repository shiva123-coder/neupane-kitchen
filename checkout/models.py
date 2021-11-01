import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from menu.models import Item
from profiles.models import UserProfile


class Order(models.Model):
    """ create order model"""
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="orders")
    full_name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    contact_number = models.CharField(max_length=11, null=False, blank=False)
    street_address = models.CharField(max_length=60, null=False, blank=False)
    postal_code = models.CharField(max_length=10, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    sum_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default="")
    stripe_payment_intent_id = models.CharField(max_length=254,
                                                blank=False, default="")

    def _make_order_number(self):
        """
        utilize UUID to create random order number
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override original save method and set the order number
        if not set.
        """
        if not self.order_number:
            self.order_number = self._make_order_number()
        super().save(*args, **kwargs)

    def update_sum_total(self):
        """
        Update sub-total each time a new line item is added
        """
        self.total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.total < settings.FREE_DELIVERY_OUTSET:
            self.delivery_cost = self.total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.sum_total = self.total + self.delivery_cost
        self.save()

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    item = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Tag: {self.item.tag} on order {self.order.order_number}"
