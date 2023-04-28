from django.urls import path
from . import views

urlpatterns = [
    path("",views.StartingPageView.as_view(),name="starting-page"),
    path("create",views.CreateView.as_view(),name="create-post-page"),
    path("register",views.AuthorView.as_view(),name="register-page"),
    path("all-authors",views.AllAuthorView.as_view(),name="all-authors-page"),
    path("posts/<slug:slug>",views.SinglePostView.as_view(),name="single-post-page"),

]
