from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from rest_framework import viewsets, generics

# Create your views here.
#


from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def 



# class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


#class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
# class CategoryView(View):
#
#     def get(self, request):
#         cats = Category.objects.all()
