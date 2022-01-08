from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    # inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "full_name",
        "contact_number",
        "email",
        "message",
        "date"
    )

    fields = (
        "full_name",
        "contact_number",
        "email",
        "message",
        "date"
    )

    list_display = (
       "full_name",
       "contact_number",
       "email",
       "message",
       "date"
    )

    ordering = (
        "-date",
    )


admin.site.register(Message, MessageAdmin)
