from django.db import models


# Models for tasks 1, 2, 3

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course', related_name='students', blank=True)


class Course(models.Model):
    title = models.CharField(max_length=100, blank=True)


# Task 4 Models

class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    article = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateField(auto_now_add=True, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class User(models.Model):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True)
    paid = models.BooleanField(default=False, blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class OrderItem(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, blank=True, null=True)
