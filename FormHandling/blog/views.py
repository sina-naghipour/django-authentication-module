from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm
from django.http import HttpResponse
from blog.models import Post, Category


class PostList(LoginRequiredMixin, View):
    template_name = 'post_list.html'
    def get(self, request):
        user = request.user
        posts = Post.objects.filter(author=user)
        return render(request, self.template_name, {'posts' : posts})


class PostDetail(LoginRequiredMixin, View):
    template_name = 'post_detail.html'
    def get(self, request, pk):
        user = request.user
        post = Post.objects.get(pk=pk)
        return render(request,self.template_name, {'post' : post})
    

class PostUpload(LoginRequiredMixin, View):
    template_name = 'post_form.html'
    form_class = PostForm
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            try :            
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                status = form.cleaned_data['status']
                image = form.cleaned_data['image']
                categories = form.cleaned_data['categories'].split(',')
                for category in categories:
                    if not Category.objects.filter(title=category):
                        categ = Category(title=category)
                        categ.save()

                post = Post(title=title, content=content, status=status, image=image, author=user)
                post.save()
                post.tags.add(*Category.objects.filter(title__in=categories))
            except :
                return redirect('blog:post_upload')
                         
            return redirect('blog:post_list')
        else:
            return redirect('blog:post_upload')
        