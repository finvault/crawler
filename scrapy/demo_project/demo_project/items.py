# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags, strip_html5_whitespace
from scrapy.loader import ItemLoader


class FirstHalf:

    def __call__(self, values):
        # length = len(values)
        # middle_index = length // 2
        # return values[:middle_index]
        return values
        
class SecondHalf:

    def __call__(self, values):
        # length = len(values)
        # middle_index = length // 2
        # return values[middle_index:]
        return values

class Slice():
    def __init__(self, index):
        self.index = index
    def __call__(self, list):
        return list[self.index]


class CustomLoader(ItemLoader):
    no_duplicate = set()
    default_input_processor = MapCompose(remove_tags, strip_html5_whitespace)

    # remove duplicate items in return data
    def load_item(self):  
        item = self.item

        for field_name in tuple(self._values):
            if field_name in self.no_duplicate:
                continue
            else:
                self.no_duplicate.add(field_name)
                value = self.get_output_value(field_name)
                if value is not None:
                    item[field_name] = value
                
        if len(item.keys()) != 0:
            return item



class FixedMortgageItem(scrapy.Item):
    fix_insured_mortgage_rate = scrapy.Field(
        output_processor = FirstHalf()
    )

    fix_conventional_mortgage_rate = scrapy.Field(
        output_processor = SecondHalf()
    )

    fix_insured_mortgage_rate_time = scrapy.Field(
        output_processor = FirstHalf()
    )

    fix_conventional_mortgage_rate_time = scrapy.Field(
        output_processor = SecondHalf()
    )


        