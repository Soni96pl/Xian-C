# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime


import xiandb as db


class StorySpider(scrapy.Spider):
    name = 'story'
    allowed_domains = ['www.wikitravel.org']

    def __init__(self, _ids):
        _ids = map(int, _ids.split(','))
        self.cities = db.City.find({'_id': {'$in': _ids}})

    def prepare_request(self, city):
        return scrapy.FormRequest(
            url='http://wikitravel.org/wiki/en/api.php',
            formdata={'action': 'parse',
                      'page': city['name'],
                      'format': 'json'},
            meta={'db': city}
        )

    def start_requests(self):
        return map(self.prepare_request, self.cities)

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        error = data.get('error', None)
        if error:
            if error == "The page you specified doesn't exist":
                return {
                    'db': response.meta['db'],
                    'story': {
                        'content': '',
                        'existing': False,
                        'updated': datetime.now()
                    }
                }
        else:
            hxs = scrapy.Selector(text=data['parse']['text']['*'])
            return {
                'db': response.meta['db'],
                'story': {
                    'content': hxs.xpath('(//p)[2]').extract_first(),
                    'existing': True,
                    'updated': datetime.now()
                }
            }
