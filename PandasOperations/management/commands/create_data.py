import pandas as pd
import re
from django.core.management import BaseCommand
from django.conf import settings

from Styling.models import Garments, ImageURLs, Images, ProductCategories


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
        garments = self.sanitize.sanitize_garment_data()[:1000]
        pattern = re.compile('[^a-zA-Z]')

        for garment in garments.iterrows():
            gar = Garments(
                product_id=garment[1].product_id,
                brand=pattern.sub('', garment[1].brand).upper(),
                gender=garment[1].gender,
                price=garment[1].price,
                product_description=garment[1].product_description,
                product_title=garment[1].product_title,
                source=garment[1].source,
                url=garment[1].url,
            )
            gar.save()

            for url in garment[1].image_urls:
                img_urls = ImageURLs(
                    image_url=url,
                    garment=gar
                )
                img_urls.save()

            for product_category in garment[1].product_categories:
                product_category = ProductCategories(
                    product_category=pattern.sub('', product_category).upper(),
                    garment=gar
                )
                product_category.save()

            for image in garment[1].images:
                image = Images(
                    url=image['url'],
                    path=image['path'],
                    checksum=image['checksum'],
                    garment=gar
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
