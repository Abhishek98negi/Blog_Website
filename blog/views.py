from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from django.urls import reverse
from .forms import AuthorForm, PostForm, CommentForm
from .models import Post,Author
# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AllAuthorView(ListView):
    template_name = "blog/all_authors.html"
    model = Author
    context_object_name = "authors"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SinglePostView(View):
   
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context={
            "post" : post,
            "author": post.author,
            "comment_form": CommentForm(),
            "comments":post.comments.all().order_by("-id") # type: ignore
        }
        return render(request, "blog/single_post.html",context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("single-post-page", args=[slug])) 
        
        context={
            "post" : post,
            "author": post.author,
            "comment_form": comment_form,
            "comments":post.comments.all().order_by("-id") # type: ignore
        }
        return render(request, "blog/single_post.html",context)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["comment_form"] = CommentForm()
    #     context["author"] = self.object.author # type: ignore
    #     return context


class AuthorView(View):

    def get(self,request):
        author = AuthorForm()
        return render(request, 'blog/register.html', {
            "author": author
        })
    
    def post(self,request):
        author = AuthorForm(request.POST,request.FILES)

        if author.is_valid():
            author.save()
            return HttpResponseRedirect("/")
        return render(request, 'blog/register.html', {
            "author": author
        })


class CreateView(View):

    def get(self,request):
        form = PostForm()
        return render(request, 'blog/create_blog.html', {
            "form":form
        })
    
    def post(self,request):
        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

        return render(request, 'blog/create_blog.html', {
            "form":form
        })
    

    