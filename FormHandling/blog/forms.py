from django import forms
from blog.models import Post
from django.core.validators import FileExtensionValidator


class PostForm(forms.Form):
    title = forms.CharField(max_length=120)
    content = forms.CharField()
    status = forms.ChoiceField(choices=Post.StatusChoices.choices)
    image = forms.ImageField()
    categories = forms.CharField(max_length=255)
    
    class Meta:
        fields = ['title', 'content', 'status', 'image', 'categories']
        labels = {
            'title' : 'title',
            'content' : 'content',
            'status' : 'status',
            'image' : 'image',
            'categories' : 'categories',
        }
        
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'content' : forms.TextInput(attrs={'class' : 'form-control'}),
            'status' : forms.Select(choices=Post.StatusChoices.choices,attrs={'class' : 'form-control'}),
            'image' : forms.FileInput(attrs={'class' : 'form-control'}),
            'categories' : forms.TextInput(attrs={'class' : 'form-control'})
        }
        validators = [
            FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])
        ]