import json
import re

from django.core.management import BaseCommand

from .create_data import SanitizeData

class Command(BaseCommand):

    def __init__(self):
        self.sanitize = SanitizeData()
        self.brand_mapping = []


    def execute(self, *args, **options):
        pattern = re.compile('[^a-zA-Z]')

        garments = self.sanitize.sanitize_garment_data()
        brands = garments['brand'].unique()

        with open('Styling/Data/brandMapping.txt', 'w', encoding=('utf-8-sig')) as brandsmap:

            for brand in brands:
                brandUPPER = pattern.sub('', brand).upper()
                brandTUPLE = (brandUPPER, brand)
                self.brand_mapping.append(brandTUPLE)


            brandsmap.write("BRANDS_MAPPING = (\n\t" + ",\n\t".join(str(x) for x in self.brand_mapping) + "\n)")