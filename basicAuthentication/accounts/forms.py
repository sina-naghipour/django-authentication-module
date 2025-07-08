from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']
        
        widgets = {
            'email' : forms.TextInput(attrs={'class' : 'form-control'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
        
            'password1' : forms.PasswordInput(attrs={'class' : 'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class' : 'form-control'}),
        }
        
        labels = {
            'email' : 'email',
            'first_name' : 'first_name',
            'last_name' : 'last_name',
            'username' : 'username',
            'password1' : 'password1',
            'password2' : 'password2',
        }