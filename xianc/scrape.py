from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import os
import wikitravel


def story(city):
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'xianc.wikitravel.settings'
    process = CrawlerProcess(get_project_settings())
    process.crawl(wikitravel.spiders.story.StorySpider,
                  name=city['name'],
                  _id=city['_id'])
    process.start()


__all__ = ['story']
