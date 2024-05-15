
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
from django.contrib import admin

from .models import Category, User, Route, Buses


class UserForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'is_staff', 'avatar', 'status']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'avatar']
    search_fields = ['id', 'first_name', 'last_name', 'email', ]
    form = UserForm



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
admin.site.register(Route)
admin.site.register(Buses)
admin.site.register(User, UserAdmin)