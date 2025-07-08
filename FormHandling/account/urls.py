from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('', home, name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/',Logout.as_view(), name='logout'),
    path('register/',Register.as_view(), name='register'),
]