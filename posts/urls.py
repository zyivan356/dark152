from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:post_id>/', views.post, name="post"),
    path('news/', views.news, name="news"),
    path('post_create/', views.post_create, name="post_create"),

]