from django.urls import path
from .views import home, RegisterView

app_name = 'blog'
urlpatterns = [
    path('', home, name='blog-home'),
    path('register/', RegisterView.as_view(), name='blog-register'),
    path('about/', RegisterView.as_view(), name='about'),
    path('chat/', RegisterView.as_view(), name='chat'),
    path('login/', RegisterView.as_view(), name='login'),
    path('logout/', RegisterView.as_view(), name='logout')
]