from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
from random import randint
from django.utils.text import slugify



class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_image = models.ImageField(upload_to="authors_images",null=True)
    about_author = models.TextField(validators=[MinLengthValidator(10)])
    email_address = models.EmailField()

    def __str__(self):
        return self.author_name
    

class Post(models.Model):
    title = models.CharField(max_length=150)
    blog_image = models.ImageField(upload_to="blogs_images",null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts") 
    
    def save(self, *args, **kwargs):
        if Post.objects.filter(title=self.title).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.title) + "-" + extra
        else:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


