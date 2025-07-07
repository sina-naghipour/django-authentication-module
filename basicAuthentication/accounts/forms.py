from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        
        fields = ['username', 'password']
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control'})
        }
        
        labels = {
            'username' : 'Username',
            'password' : 'Password'
        }

