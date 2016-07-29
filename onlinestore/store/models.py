from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    """Create base model for Stores."""

    STORE_TYPE_CHOICES = (
        ('education', 'Education'),
        ('fashion', 'Fashion'),
        ('food', 'Food'),
        ('furniture', 'Furniture'),
        ('electronics', 'Electronics'),
        ('beauty', 'Beauty'),
        ('', 'No category set'),
    )

    store_name = models.CharField(max_length=250)
    picture = models.ImageField(
        upload_to='stores/', default='img/nopic.png')
    store_type = models.CharField(max_length=25, choices=STORE_TYPE_CHOICES,)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        """Display string representation of storename."""
        return self.store_name


class Product(models.Model):
    """Create base model for Products."""

    product_name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='products/')
    store = models.ForeignKey(Store)

    def __unicode__(self):
        """Display string representation of a product name."""
        return self.product_name
