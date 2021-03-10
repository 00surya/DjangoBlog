from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('about/<str:slug>', views.aboutauthor, name='aboutAuthor'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='singup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]