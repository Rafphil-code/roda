from django.contrib import admin
from .models import Product, Category, Service, CustomUser, OtpToken
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(CustomUser)
admin.site.register(OtpToken)