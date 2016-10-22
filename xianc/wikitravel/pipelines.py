# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import xiandb as db


class WikitravelPipeline(object):
    def process_item(self, item, spider):
        city = db.City.find_one({'_id': item['_id']})
        city['story'] = item['story']
        city.save()
