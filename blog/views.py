from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import FeedbackForm, PostForm
from .models import Post, Feedback


def blog(request):
    """
    view to the blog page
    """
    posts = Post.objects.all()
    template = 'blog/blog.html'

    context = {
        'posts': posts,
    }

    return render(request, template, context)


