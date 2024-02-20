
from django.contrib import admin
from django.urls import path
# from . import views
from .views import HomeView, ArticleDetail, AddPost, UpdatePost, DeletePost

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article"),
    path('add-post/', AddPost.as_view(), name='add-post'),
    path('update-post/<int:pk>', UpdatePost.as_view(), name='update-post'),
    path('delete-post/<int:pk>', DeletePost.as_view(), name='delete-post'),
]
