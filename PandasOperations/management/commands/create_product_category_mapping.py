import re

from django.core.management import BaseCommand

from .create_data import SanitizeData

class Command(BaseCommand):

    def __init__(self):
        self.sanitize = SanitizeData()
        self.product_categories = []
        self.product_category_mapping = []


    def execute(self, *args, **options):
        garments = self.sanitize.sanitize_garment_data()
        pattern = re.compile('[^a-zA-Z]')
        product_categories = garments['product_categories']

        with open('Styling/Data/productCategoryMapping.txt', 'w') as productcategoriessmap:

            for product_category_list in product_categories:
                for product_category in product_category_list:
                    if product_category not in self.product_categories:
                        self.product_categories.append(product_category)

                        product_categoryUPPER = pattern.sub('', product_category).upper()
                        product_category_TUPLE = (product_categoryUPPER, product_category)

                        self.product_category_mapping.append(product_category_TUPLE)

            productcategoriessmap.write("PRODUCT_CATEGORIES_MAPPING = (\n\t" + ",\n\t".join(str(x) for x in self.product_category_mapping) + "\n)")
