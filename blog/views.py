from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, FormView
from django.views.generic.detail import DetailView
from .forms import AuthorForm, PostForm
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



class SinglePostView(DetailView):
    template_name = "blog/single_Post.html"
    model = Post
    context_object_name = "post" 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = self.object.author # type: ignore
        return context


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
    

    