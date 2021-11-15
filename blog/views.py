from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    view to add comment to the post
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


@login_required
def delete_comment(request, post_id):
    """
    view to delete comment
    """
    comment = get_object_or_404(Comment, pk=post_id)
    comment.delete()
    messages.success(request, 'Your comment has now deleted')
    return redirect(reverse('post_info', args=(comment.post.id,)))


@login_required
def add_post(request):
    """
    add post to the blog page
    option only for superuser
    """
    if not request.user.is_superuser:
        messages.warning(request, 'Access denied, \
             only admin has access to this page')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you!,\
                 Post added the blog succesfully!')
            return redirect(reverse('blog'))
        else:
            messages.error(request,
                           ('Sorry! Something went wrong,\
                                Please recheck the form and try again.'))
    else:
        form = PostForm()

    template = 'blog/add_post.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """edit/update post and its info from the page"""
    if not request.user.is_superuser:
        messages.warning(request, 'Access denied,\
             only admin has access to this')
        return redirect(reverse('blog'))
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Succesfully updated!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Sorry, request failed,\
                 please re-check the form and try again')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
        'on_edit_page': True
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Delete post from the page """
    if not request.user.is_superuser:
        messages.warning(request, 'Access denied,\
             only admin has access to this')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
