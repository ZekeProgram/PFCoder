from django.urls import path
from .views import home, RegisterView, CustomLoginView, contact, login, about, crear
from blog import views


app_name = 'blog'
urlpatterns = [
    path('', home, name='blog-home'),
    path('register/', RegisterView.as_view(), name='blog-register'),
    path('about/',about , name='about'),
    path('chat/', RegisterView.as_view(), name='chat'),
    path('login/', login, name='login'),
    path('logout/', RegisterView.as_view(), name='logout'),
    path('submit/', RegisterView.as_view(), name='submit'),
    path('contact/', contact, name='contact'),
    path('crear/', crear, name= 'crear',)
]