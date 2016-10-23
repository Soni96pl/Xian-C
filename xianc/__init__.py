import os
from datetime import datetime

from redis import Redis
from rq_scheduler import Scheduler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import wikitravel


scheduler = Scheduler(connection=Redis())


class CrawlerManager(object):
    storage = Redis()

    def crawl(self):
        os.environ['SCRAPY_SETTINGS_MODULE'] = self.module + '.settings'
        process = CrawlerProcess(get_project_settings())
        spiders = self.storage.smembers('spiders')
        for spider in spiders:
            _ids = self.storage.smembers(spider)
            if _ids:
                self.storage.delete(spider)
                process.crawl(self.spiders[spider], _ids=','.join(_ids))
        process.start()


class Wikitravel(CrawlerManager):
    module = 'xianc.wikitravel'
    spiders = {'story': wikitravel.spiders.story.StorySpider}

    def __init__(self):
        self.storage.sadd('spiders', 'story')
        self.schedule = scheduler.schedule(
            scheduled_time=datetime.utcnow(),
            func=self.crawl,
            interval=5,
            repeat=None
        )

    def story(self, _id):
        self.storage.sadd('story', _id)


__all__ = ['Wikitravel']
