from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = (
        "lineitem_total",
    )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "discount_percent",
        "discount_amount",
        "total",
        "sum_total",
        "payment_method",
        "original_basket",
        "stripe_payment_intent_id"
    )

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "contact_number",
        "street_address",
        "postal_code",
        "delivery_cost",
        "payment_method",
        "discount_percent",
        "discount_amount",
        "total",
        "sum_total",
        "original_basket",
        "stripe_payment_intent_id"
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "total",
        "delivery_cost",
        "discount_percent",
        "discount_amount",
        "sum_total",
    )

    ordering = (
        "-date",
    )


admin.site.register(Order, OrderAdmin)
