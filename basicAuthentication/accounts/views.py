from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import LoginForm

class Login(View):
    
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        user = request.user
        form = self.form_class()
        
        if isinstance(user, AnonymousUser):
            return render(request, self.template_name, {'form' : form})
        else:
            if user.is_authenticated:
                return redirect('accounts:dashboard')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            form = self.form_class()
            messages = [
                {'tags': 'error', 'content' : 'login failed'}
            ]
            return render(request, self.template_name, {'form' : form, 'messages' : messages})

class Logout(LoginRequiredMixin, View):
    
    template_name = 'logout.html'
    
    def get(self, request):
        user = request.user
        if isinstance(user, AnonymousUser):
            return redirect('accounts:login')
        
        return HttpResponse('Logout')




class Register(View):
    
    template_name = 'register.html'
    
    def get(self, request):
        user = request.user
        if not isinstance(user, AnonymousUser):
            return redirect('accounts:login')
        else:
            return HttpResponse('Register')


class Dashboard(LoginRequiredMixin, View):
    pass