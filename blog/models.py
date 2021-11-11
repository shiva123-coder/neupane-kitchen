from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    blogger = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, max_length=500)

    class Meta:
        ordering = ['-date']
