from django.urls import path, include
from blog import views
urlpatterns = [
    path('postComment/',views.postComment,name="postComment"),
    path('', views.bloghome, name='home'),
    path('<str:slug>', views.blogPost, name='blogPost'),
    # Api to post a comment

]