# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime


import xiandb as db


class StorySpider(scrapy.Spider):
    name = 'story'
    allowed_domains = ['www.wikitravel.org']

    def __init__(self, _id, name=None):
        self._id = int(_id)
        if not name:
            name = db.City.find_one({'_id': self._id}, {'name': 1})['name']
        self.name = name

    def start_requests(self):
        return [scrapy.FormRequest(
            url='http://wikitravel.org/wiki/en/api.php',
            formdata={'action': 'parse', 'page': self.name, 'format': 'json'},
            meta={'_id': self._id, 'name': self.name}
        )]

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        error = data.get('error', None)
        if error:
            if error == "The page you specified doesn't exist":
                return {
                    '_id': response.meta['_id'],
                    'story': {
                        'content': '',
                        'existing': False,
                        'updated': datetime.now()
                    }
                }
        else:
            hxs = scrapy.Selector(text=data['parse']['text']['*'])
            return {
                '_id': response.meta['_id'],
                'story': {
                    'content': hxs.xpath('(//p)[2]').extract_first(),
                    'existing': True,
                    'updated': datetime.now()
                }
            }
