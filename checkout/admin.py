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
        "total",
        "sum_total",
    )

    fields = (
        "order_number",
        "date",
        "full_name",
        "email",
        "contact_number",
        "address",
        "door_no",
        "town_or_city",
        "postcode",
        "delivery_cost",
        "total",
        "sum_total",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "total",
        "delivery_cost",
        "sum_total",
    )

    ordering = (
        "-date",
    )


admin.site.register(Order, OrderAdmin)