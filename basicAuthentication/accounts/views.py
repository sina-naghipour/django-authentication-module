from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    return redirect('accounts:login')
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
        else:
            if user.is_authenticated:
                logout(request)
            return redirect('accounts:login')


class Register(View):
    template_name = 'register.html'
    form_class = RegisterForm
    
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('accounts:dashboard')
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            return redirect('accounts:register')
            
        try:
            # Use create_user instead of create to properly hash the password
            user = User.objects.create_user(
                email=email,
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password1
            )
            
            # Log the user in after successful registration
            login(request, user)
            return redirect('accounts:dashboard')
            
        except Exception as e:
            print(e)  # For debugging
            return redirect('accounts:register')


class Dashboard(LoginRequiredMixin, View):
    template_name = 'dashboard.html'
    login_url = '../login/'
    
    def handle_no_permission(self):
        return redirect(self.login_url)
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('accounts:login')