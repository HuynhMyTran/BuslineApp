from django.contrib import admin

# Register your models here.
from .models import Category, Route, Receipt

admin.site.register(Category)
admin.site.register(Route)
admin.site.register(Receipt)