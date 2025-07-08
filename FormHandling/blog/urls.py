from django.urls import path
from django.views import View
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('post/list/',PostList.as_view(), name='post_list'),
    path('post/upload/',PostUpload.as_view(), name='post_upload'),
]