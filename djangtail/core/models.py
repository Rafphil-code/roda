from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import secrets
from django.conf import settings

#On personnalise la classe User 

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

# Modèle Category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nom de la catégorie
    description = models.TextField(blank=True, null=True)  # Description de la catégorie
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création

    def __str__(self):
        return self.name

# Modèle Product
class Product(models.Model):
    name = models.CharField(max_length=255)  # Nom du produit
    description = models.TextField()  # Description du produit
    image_url = models.ImageField(upload_to='products/', blank=True, null=True)  # Image du produit
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix du produit en FCFA
    popular = models.BooleanField(default=False)  # Marque ce produit comme populaire ou non
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  # Catégorie du produit
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création

    def __str__(self):
        return self.name

    
class UserItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.product.name


# Modèle Service
class Service(models.Model):
    name = models.CharField(max_length=255)  # Nom du service
    description = models.TextField()  # Description du service
    image_url = models.ImageField(upload_to='services/', blank=True, null=True)  # Image du service
    price = models.DecimalField(max_digits=10, decimal_places=3)  # Prix du service en FCFA
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    icon = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class OtpToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="otps")
    otp_code = models.CharField(max_length=6, default=secrets.token_hex(3))
    otp_created_at = models.DateTimeField(auto_now_add=True)
    otp_expires_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
