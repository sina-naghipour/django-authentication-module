from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import Product, Review
from products.serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination


class List(ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = ProductSerializer
    queryset = Product.objects.all()