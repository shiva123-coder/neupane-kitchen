from django.db import models
from django.utils import timezone

from profiles.models import UserProfile
from menu.models import Item


class Review(models.Model):
    RATE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    reviewer = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    title = models.CharField(null=False, blank=True, max_length=50)
    comment = models.TextField(null=False, blank=False, max_length=300)
    rating = models.IntegerField(choices=RATE)
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f'{self.reviewer}'
