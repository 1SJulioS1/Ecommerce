from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


phone_regex = r'^\+53\d{1}\d{7}$'
phone_validator = RegexValidator(
    regex=phone_regex,
    message="El número de teléfono debe tener el siguiente formato: '+código de país-número de área-número de teléfono'."
)


class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    extra_info = models.TextField(
        max_length=300, blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.number}, {self.street}, {self.city}, {self.state}, {self.country}'


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Administrador'),
        ('regular_user', 'Usuario regular'),
    )
    email = models.EmailField(unique=True)
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default='regular_user')
    phone = models.CharField(
        max_length=20,
        validators=[phone_validator]
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,  blank=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'


class Courier(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=20,
        validators=[phone_validator]
    )
    availability = models.BooleanField(default=True)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, through='OrderItem')
    address = models.ForeignKey(Address, models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    courier = models.ForeignKey(Courier, on_delete=models.PROTECT)

    def __str__(self):
        return f'Order #{self.id}'

    def get_total_price(self):
        order_items = OrderItem.objects.filter(order=self)
        total_price = sum(item.product.price *
                          item.quantity for item in order_items)
        return total_price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'
