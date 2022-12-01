from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.index, name='homepage'),
    path('posts/', views.group_posts, name='group_list')

]
