from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category, User, Buses, Route


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        # fields = ['id', 'name', 'created_date', 'description']
        fields = '__all__'


class RouteSerializer(ModelSerializer):
    class Meta:
        model = Route
        # fields = ['id', 'name', 'buses', 'created_date', 'category']
        fields = '__all__'


class Buses(ModelSerializer):
    class Meta:
        model = Buses
        # fields = ['id', 'name', 'created_date']
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'first_name', 'last_name', 'avatar', 'email', 'phone_num', 'created_date']
        fields = '__all__'
