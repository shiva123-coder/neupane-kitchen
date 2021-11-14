from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import CommentForm, PostForm
from .models import Post, Comment


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


def post_info(request, post_id):
    """
    
    """
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.blogger = request.user
            comment.save()

            messages.success(request, 'Thank you,\
                your comment has been added.')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Sorry! something went wrong,\
                 please try again')
            return redirect(reverse('post_info', args=[post_id]))

    else:
        form = CommentForm()
        template = 'blog/post_info.html'
        context = {
            'post': post,
            'form': form,
        }

        return render(request, template, context)


def delete_comment(request, post_id):
    """
    view to delete comment
    """
    comment = get_object_or_404(Comment, pk=post_id)
    comment.delete()
    messages.success(request, 'Your comment has now deleted')
    return redirect(reverse('post_info', args=(comment.post.id,)))
