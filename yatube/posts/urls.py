from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index),
    path('group_post/<slug:slug>',
         views.group_posts),
    path('posts/', views.index, name='homepage')
]