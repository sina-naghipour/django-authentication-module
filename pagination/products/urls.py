from django.urls import path
from products.views import List


app_name = 'products'

urlpatterns = [
    path('list/', List.as_view(), name='list'),
]

