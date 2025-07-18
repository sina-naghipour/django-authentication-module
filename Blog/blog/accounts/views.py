from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import LoginForm, RegisterForm
from django.contrib.auth.models import AnonymousUser
from accounts.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class Login(View):
    template_name = 'login.html'
    form_class = LoginForm
    def get(self, request):
        user = request.user
        if isinstance(user, AnonymousUser):
            form = self.form_class()

            return render(request, 'login.html', {'form' : form})
        else:
            return redirect('home')
    def post(self, request):
        if not isinstance(request.user, AnonymousUser):
            return redirect('home')
        else:
            form = self.form_class(request.POST)

            if form.is_valid():
                print('valid')
                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user:
                    login(request, user)
                    messages.success(request, f'Welcome Back {user.first_name}!')
                    return redirect('core:dashboard')
                else:
                    messages.error(request, 'Wrong Credentials.')
                    return redirect('accounts:login')
            
            return redirect('accounts:login')

class Register(View):
    template_name = 'register.html'
    form_class = RegisterForm
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})    

class Logout(View):
    
    def get(self, request):
        if isinstance(request.user, AnonymousUser):
            return redirect('accounts:login')
        else:
            logout(request)
            return redirect('accounts:login')