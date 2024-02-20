from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

#ListView makes a query to db and brings a list of all records
#DetailBiew also makes query to db and returns details of a single entry
# These are class-based views

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    #fields = '__all__'

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update-post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')