from rest_framework.decorators import action
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from rest_framework import viewsets, generics, status, permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from . import models
# Create your views here.
#
from .models import Category, User, Buses, Route, Comment
from .paginator import BuslinePaginator
from .perms import CommentOwner
from .serializers import CategorySerializer, BusSerializer, UserSerializer, RouteSerializer, CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer
    paginator_class = BuslinePaginator
    # permission_classes = permissions.IsAuthenticated


class BusViewSet(viewsets.ModelViewSet, viewsets.ViewSet):
    queryset = Buses.objects.filter(active=True)
    serializer_class = BusSerializer
    paginator_class = BuslinePaginator

    def filter_queryset(self, queryset):
        q = self.request.query_params.get("q")
        if q:
            queryset = queryset.filter(subject__icontains=q)

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            queryset = queryset.filter(category_id=cate_id)

        return queryset

    @action(methods=['get'], detail=True, url_path='buses')
    def lessons(self, request, pk):
        c = self.get_object() # Buses.query.get(pk=pk)
        buses = c.lesson_set.filter(active=True)


class RouteViewSet(viewsets.ModelViewSet, ):
    queryset = Route.objects.filter(active=True)
    serializer_class = RouteSerializer
    paginator_class = BuslinePaginator




class UserViewSet(viewsets.ViewSet, generics.ListAPIView,
                      generics.RetrieveAPIView, generics.CreateAPIView,
                      generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]
    paginator_class = BuslinePaginator



class CommentViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CommentSerializer
    permission_classes = [CommentOwner, ]
