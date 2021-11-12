from django import forms
from .models import Post, Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            'feedback',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'feedback': 'write your feedback here',
        }


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

        self.fields["title"].widget.attrs["placeholder"] = "Post Title"
        self.fields["content"].widget.attrs["placeholder"] = "Post Content"
