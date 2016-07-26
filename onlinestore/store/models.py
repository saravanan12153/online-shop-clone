from __future__ import unicode_literals

from django.db import models


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
    picture = models.ImageField(upload_to='/stores/')
    store_type = models.CharField(max_length=25, choices=STORE_TYPE_CHOICES,)
