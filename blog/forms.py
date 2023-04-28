from django import forms
from .models import Post,Author


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
