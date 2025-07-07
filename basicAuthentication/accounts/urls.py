from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [

    path('login/',Login.as_view(), name='login'),
    path('logout/',Logout.as_view(), name='logout'),
    path('register/',Register.as_view(), name='register'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]