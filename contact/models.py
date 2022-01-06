from django.db import models


class Message(models.Model):
    full_name = models.CharField(
        max_length=40, null=False, blank=False, default="")
    email = models.EmailField(
        max_length=50, null=False, blank=False, default="")
    contact_number = models.CharField(
        max_length=11, null=False, blank=False, default="")
    message = models.TextField(
        max_length=300, null=False, blank=False, default="")