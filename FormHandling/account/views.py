from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model, authenticate, login, logout
from account.forms import *
# Create your views here.

User = get_user_model()

def home(request):
    return redirect('account:login')


class Login(View):
    template_name = 'login.html'
    form_class = LoginForm
    
    def get(self, request):
        user = request.user
        form = self.form_class()
        next_url = self.request.GET.get('next')
        if user.is_authenticated:
            if next_url:
                return redirect(next_url)
            return redirect('blog:post_list')
        else:
            return render(request, self.template_name, {'form' : form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('blog:post_list')
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form' : form, 'error' : 'Wrong Credentials.'})


class Register(View):
    template_name = 'register.html'
    form_class = RegisterForm
    
    def get(self, request):
        user = request.user
        if isinstance(user, AnonymousUser):
            form = self.form_class()
            return render(request, self.template_name, {'form' : form})
        else:
            return redirect('blog:post_list')

    def post(self, request):
        
        user = request.user
        
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        if password1 != password2:
            return render(request, self.template_name, {'form' : form, 'error' : 'Could not Create User, Try Again.'})
        try:
            User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
        except:
            form = self.form_class()
            return render(request, self.template_name, {'form' : form, 'error' : 'Could not Create User, Try Again.'})

        user = authenticate(request, username=username, password=password1)
        if user:
            login(request, user)
            return redirect('blog:post_list')



class Logout(View):
    
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            logout(request)
            return redirect('account:login')
        else:
            return redirect('account:login')
