from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    blogger = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.title


class Feedback(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="feedback")
    blogger = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback on {self.post.title} by {self.blogger}"
