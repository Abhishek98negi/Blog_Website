from django import forms
from .models import Post,Author,Comment


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            "author_name":"Your Name",
            "author_image":"Your Picture",
            "about_author":"About You",
            "email_address":"Your Email"
        }



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        exclude = ['slug','date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post','date']
        labels = {
            "user_name": "Name",
            "text" : "Comment"
        }
