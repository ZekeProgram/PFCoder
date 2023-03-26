from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView


def home(request):
    return render(request, 'blog/home.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key':'value'}
    template_name = 'blog/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'blog':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect(to='/')

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember:me')

        if not remember_me:
            
            self.request.session.set_expiry(0)

            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)
    
def about(request):
    return render(request, 'blog/about.html')
def submit(request):
    return render(request, 'blog/submit.html')
def contact(request):
    return render(request, 'blog/contact.html')
def login(request):
    return render(request, 'blog/login.html')
def crear(request):
    return render(request, 'blog/crear.html')