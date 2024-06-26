from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = "CUSTOMER", 'Customer'
        SELLER = "SELLER", 'Seller'
        DRIVER = "DRIVER", 'Driver'
        ADMIN = "ADMIN", 'Admin'

    base_role = Role.ADMIN

    avatar = models.ImageField(upload_to='busline/users/%Y/%m', null=True, blank=True)
    status = models.CharField(max_length=50, choices=Role.choices)
    email = models.EmailField(max_length=100, unique=True)
    description = RichTextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.Role = self.base_role
            return super().save(*args, **kwargs)


class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(status=User.Role.SELLER)


class Customer(User):
    base_role = User.Role.CUSTOMER
    customer = CustomerManager()

    class Meta:
        proxy = True


class CustomerProfile(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE, parent_link=True)


# trả user có vai trò là driver về
class DriverManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(status=User.Role.DRIVER)


class Driver(User):
    base_role = User.Role.DRIVER
    driver = DriverManager()

    class Meta:
        proxy = True


class DriverProfile(models.Model):
    user = models.OneToOneField(Driver, on_delete=models.CASCADE, parent_link=True)


class SellerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(status=User.Role.SELLER)


class Seller(User):
    base_role = User.Role.SELLER
    seller = SellerManager()

    class Meta:
        proxy = True


class SellerProfile(models.Model):
    user = models.OneToOneField(Seller, on_delete=models.CASCADE, parent_link=True)
    note = RichTextField(blank=True)


# một tài xế được lái nhiều xe
# một xe đc một tài xế lái
class Buses(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    description = RichTextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Route(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    buses = models.ForeignKey(Buses, on_delete=models.PROTECT)
    start = models.CharField(max_length=100, null=False)
    end = models.CharField(max_length=100, null=False)
    description = RichTextField(blank=True)
    travel_time = models.DateTimeField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name


class Ticket(BaseModel):
    note = models.CharField(max_length=100, unique=True)
    seller = models.ForeignKey(Seller, related_name='seller', on_delete=models.PROTECT)
    driver = models.ForeignKey(Driver, related_name='driver', on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    route = models.ForeignKey(Route, on_delete=models.PROTECT)

    def __str__(self):
        return self.total


class Comment(models.Model):
    content = models.CharField(max_length=255)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
