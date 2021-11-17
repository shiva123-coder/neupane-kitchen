from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', 'blogger')

        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'comment': 'write your comment here',
        }

        self.fields['comment'].widget.attrs[
            'placeholder'] = 'write your comment here'
        self.fields['comment'].label = False


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            'title',
            'content',
            'image',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'Post Title'
        self.fields['content'].widget.attrs['placeholder'] = 'Post Content'
