from redis import Redis
from rq import Queue

import scrape
import wikitravel


queue = Queue(connection=Redis())


def scrape_story(city):
    queue.enqueue(scrape.story, city)


__all__ = ['scrape_story', 'wikitravel']
