from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.contrib.auth.models import Permission
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.html import mark_safe

# Register your models here.
from .models import Category, User
    # , Route

# class BuslineAppAdminSite(admin.AdminSite):
#     site_header = "HỆ THỐNG QUẢN LÝ ĐẶT VÉ XE"
#
#
#     def get_urls(self):
#         return [
#                     path('busline/stats', self.stats_view)
#         ]   + super().get_urls()
#     def stat_view(self, request):
#
#
#         return TemplateResponse(request, 'admin/stats_view.html',{
#             'stats': stats
#         })


admin.site.register(Category)
# admin.site.register(Route)
admin.site.register(User)