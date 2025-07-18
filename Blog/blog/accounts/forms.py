from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
        
        }
        
        labels = {
            'username' : 'username',
            'password' : 'password',
        }

class RegisterForm(forms.Form):
    username    = forms.CharField()
    email       = forms.EmailField()
    first_name  = forms.CharField()
    last_name   = forms.CharField()
    password    = forms.CharField()
    password2   = forms.CharField()
    
    class Meta:
        widgets = {
            'username'   : forms.TextInput(attrs={'class' : 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email'      : forms.EmailInput(attrs={'class' : 'form-control'}),
            'last_name'  : forms.TextInput(attrs={'class' : 'form-control'}),
            'password'  : forms.PasswordInput(attrs={'class' : 'form-control'}),
            'password2'  : forms.PasswordInput(attrs={'class' : 'form-control'}),
        }
        
        labels = {
            'username'   : 'username',
            'password'   : 'password',
            'password2'  : 'repeat password',
            'email'      : 'email',
            'first_name' : 'first_name',
            'last_name'  : 'last_name',

        }