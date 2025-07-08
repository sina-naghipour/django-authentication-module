from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import AnonymousUser

# Create your views here.

def home(request):
    return redirect('account:login')


class Login(View):
    template_name = 'login.html'
    def get(self, request):
        user = request.user
        
        if user.is_authenticated:
            return redirect('blog:post_list')
        else:
            return render(request, self.template_name)
        
class Register(View):
    def get(self, request):
        template_name = 'register.html'
        user = request.user
        if isinstance(user, AnonymousUser):
            return render(request, self.template_name)
        else:
            return redirect('blog:post_list')


class Logout(View):
    pass


