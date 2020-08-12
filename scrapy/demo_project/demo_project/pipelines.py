# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo




class DemoProjectPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost', 27017
        )
        db = self.conn['test']
        self.collection = db['first_national_mortgage']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

            