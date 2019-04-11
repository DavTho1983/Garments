from django.db import models
from .constants import BRANDS_MAPPING, PRODUCT_CATEGORIES_MAPPING

class Garments(models.Model):

    GENDERS = (
        ('women', 'women'),
        ('men', 'men'),
        ('trans', 'trans')
    )


    product_id = models.CharField(max_length=255, primary_key=False)
    brand = models.CharField(max_length=255, choices=BRANDS_MAPPING)
    gender = models.CharField(max_length=255, choices=GENDERS)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_description = models.CharField(max_length=255)
    product_title = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


class ImageURLs(models.Model):

    garment = models.ForeignKey(Garments, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)


class ProductCategories(models.Model):

    garment = models.ForeignKey(Garments, on_delete=models.CASCADE)
    product_category = models.CharField(max_length=255, choices=PRODUCT_CATEGORIES_MAPPING)


class Images(models.Model):

    garment = models.ForeignKey(Garments, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    checksum = models.CharField(max_length=255)