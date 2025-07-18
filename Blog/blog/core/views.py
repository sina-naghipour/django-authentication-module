from django.shortcuts import render
from django.views import View



def home(request):
    return render(request, 'home.html')


class PostDetail(View):
    pass

class PostList(View):
    pass

class PostCreate(View):
    pass


class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard.html')


class Profile(View):
    def get(self, request):
        return render(request, 'profile.html')
