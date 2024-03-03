from django.contrib.auth.models import User
from django.db import models


class Shop(models.Model):
    material_options = (
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('platinum', 'Platinum'),
        ('bronze', 'Bronze'),
        ('other', 'Other')
    )
    type_options = (
        ('rings', 'Rings'),
        ('necklaces', 'Necklaces'),
        ('earrings', 'Earrings'),
        ('bracelets', 'Bracelets'),
        ('anklets', 'Anklets'),
        ('sets', 'Sets'),
        ('other', 'Other')

    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    description1 = models.TextField()
    description2 = models.TextField(blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    description4 = models.TextField(blank=True, null=True)
    description5 = models.TextField(blank=True, null=True)
    description6 = models.TextField(blank=True, null=True)
    description7 = models.TextField(blank=True, null=True)
    description8 = models.TextField(blank=True, null=True)
    description9 = models.TextField(blank=True, null=True)
    description10 = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    material = models.CharField(max_length=8, choices=material_options, default='gold')
    type = models.CharField(max_length=9, choices=type_options, default='rings')
    img_uploaded = models.ImageField(upload_to='shop_photos/', null=True)

    def __str__(self):
        return f"{self.title}"


