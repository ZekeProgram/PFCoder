from django.urls import path
from .views import home, RegisterView, CustomLoginView, contact, login, about, crear, logout, chat, submit
from blog import views


app_name = 'blog'
urlpatterns = [
    path('', home, name='blog-home'),
    path('register/', RegisterView.as_view(), name='blog-register'),
    path('about/',about , name='about'),
    path('chat/', chat, name='chat'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('submit/', submit, name='submit'),
    path('contact/', contact, name='contact'),
    path('crear/', crear, name= 'crear',)
]