from django.contrib import admin

# Register your models here.
from models import Store, Product

admin.site.register(Store)
admin.site.register(Product)
