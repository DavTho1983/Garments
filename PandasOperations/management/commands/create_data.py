import pandas as pd
from django.core.management import BaseCommand
from django.conf import settings

from Styling.models import Garments, ImageURLs, Images


class SanitizeData:

    def __init__(self):
        self.csv_path = settings.GARMENTS_DATA_URL + '\garment_items.jl'
        self.garments = pd.read_json(self.csv_path, lines=True)


    def sanitize_garment_data(self):
        """There are no empty cells in this data so I didn't bother writing code to account for them"""
        self.garments['brand'] = self.garments.brand.astype('category')
        self.garments['gender'] = self.garments.gender.astype('category')
        self.garments['price'] = self.garments.price.str.replace(',', '').astype(float)

        return self.garments


class Command(BaseCommand):

    def __init__(self):
        self.sanitize = SanitizeData()


    def execute(self, *args, **options):
        garments = self.sanitize.sanitize_garment_data()
        print(garments['url'])

        for garment in self.garment.iterrows():
            gar = Garments(
                brand=garment['brand'],
                gender=garment['gender'],
                price=garment['price'][0],


            )
            gar.save()

            for url in garment['img_urls']:
                img_urls = ImageURLs(
                    image_url=url,
                    garments=gar
                )
                img_urls.save()

            for product_category in garment['product_categories']:
                product_category = ProductCategories(
                    product_category=product_category,
                    garments=gar
                )
                image.save()

            for image in garment['images']:
                image = Images(
                    url=image[0]['url'],
                    path=image[0]['path'],
                    checksum=image[0]['checksum'],
                    garments=gar
                )
                image.save()

        # (64134, 13)
        # brand
        # gender
        # image_urls
        # images
        # price
        # product_categories - category
        # product_categories_mapped - category
        # product_description
        # product_id
        # product_imgs_src
        # product_title
        # source
        # url
