from django.urls import path
from core.views import PostList, PostDetail, PostCreate, Dashboard, Profile
app_name = 'core'

urlpatterns = [
    path('post/list/', PostList.as_view(), name='post_list'),
    path('post/detail/', PostDetail.as_view(), name='post_detail'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('profile/', Profile.as_view(), name='profile'),
]
