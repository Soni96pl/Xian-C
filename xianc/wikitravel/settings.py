# -*- coding: utf-8 -*-

# Scrapy settings for wikitravel project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wikitravel'
USER_AGENT = 'wikitravel (+http://chronow.ski)'
ROBOTSTXT_OBEY = False
DOWNLOAD_TIMEOUT = 20
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
ITEM_PIPELINES = {
    'xianc.wikitravel.pipelines.WikitravelPipeline': 300,
}
