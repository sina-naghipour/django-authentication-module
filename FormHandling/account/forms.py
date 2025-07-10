from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username' : 'username', 'password' : 'password'}
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control'})
        }


class RegisterForm(UserCreationForm):
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2' , 'email', 'first_name', 'last_name']
        
        labels = {
        
            'username' : 'username',
            'password1' : 'password1',
            'password2' : 'password2',
            'email' : 'email',
            'first_name' : 'first_name',
            'last_name' : 'last_name'
        
        }
        widgets = {
        
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class' : 'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class' : 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
        
        }

