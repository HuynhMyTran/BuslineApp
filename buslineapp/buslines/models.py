from django.db import models
from ckeditor.fields import RichTextField



class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='users/%Y/%m', null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_num = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Route(BaseModel):
    buses = models.CharField(max_length=100, unique=True)
    description = RichTextField()

    def __str__(self):
        return self.buses


class Receipt(BaseModel):
    description = RichTextField()