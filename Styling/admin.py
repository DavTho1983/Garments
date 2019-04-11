from django.contrib import admin

from .models import Garments, ImageURLs, ProductCategories, Images


@admin.register(Garments)
class GarmentsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_title', 'brand', 'product_description')

    class Meta:
        ordering = ['product_title']

@admin.register(ProductCategories)
class ProductCategories(admin.ModelAdmin):
    list_display = ('garment_product_id', 'garment_product_title', 'product_category')

    class Meta:
        ordering = ['garment_product_title']

    def garment_product_id(self, obj):
        return obj.garment.product_id

    def garment_product_title(self, obj):
        return obj.garment.product_title


@admin.register(Images)
class Images(admin.ModelAdmin):
    list_display = ('garment_product_id', 'garment_product_title', 'url')

    class Meta:
        ordering = ['garment_product_title']

    def garment_product_id(self, obj):
        return obj.garment.product_id

    def garment_product_title(self, obj):
        return obj.garment.product_title