"""buslineapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import ckeditor_uploader
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from buslines import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('buses', views.BusViewSet, basename='buses')
router.register('users', views.UserViewSet, basename='users')
# router.register('categories_view_detail', views.CategoryView, basename='categories')
#     # ('categories', views.CategoryViewSet, basename='categories')


schema_view = get_schema_view(
    openapi.Info(
        title="Busline API",
        default_version='v1',
        description="APIs for BuslineApp",
        contact=openapi.Contact(email="tran1951052210@ou.edu.vn"),
        license=openapi.License(name="Huỳnh Mỹ Trân - Lê Thị Kiều Như @2023"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('o/', include('oauth2_provider.urls',
                       namespace='oauth2_provider')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),

]
