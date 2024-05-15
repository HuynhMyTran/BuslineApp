from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category, User, Buses, Route, Comment


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_date', 'updated_date', 'description']


class RouteSerializer(ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'name', 'buses', 'created_date', 'start', 'end','description','travel_time','price']


class BusSerializer(ModelSerializer):
    class Meta:
        model = Buses
        # fields = ['id', 'name', 'created_date']
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % obj.image.name) if request else ''


class UserSerializer(ModelSerializer):
    image = serializers.SerializerMethodField(source='avatar')

    def get_image(self, obj):
        if obj.avatar:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % obj.avatar.name) if request else ''

    def create(self, validated_data):
        data = validated_data.copy()
        u = User(**data)
        u.set_password(u.password)
        u.save()
        return u

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'avatar', 'image']
        extra_kwargs = {
            'password': {'write_only': 'True'}
        }


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_date', 'user']