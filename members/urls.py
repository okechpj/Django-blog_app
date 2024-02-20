
from django.contrib import admin
from django.urls import path
from . import views
from .views import UserReristerView


urlpatterns = [
   path('register/', UserReristerView.as_view(), name='register'),
   path('logout/', views.userLogout, name='logout')
]
