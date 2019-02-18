from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('<int:blog_id>/edit/', views.edit, name="edit"),
    path('<int:blog_id>/delete/', views.delete, name="delete"),
]
