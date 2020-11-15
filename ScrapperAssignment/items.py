# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import json

import scrapy
import six
from collections import OrderedDict


class OrderedItem(scrapy.Item):
    def __init__(self, *args, **kwargs):
        self._values = OrderedDict()
        if args or kwargs:  # avoid creating dict for most common case
            for k, v in six.iteritems(dict(*args, **kwargs)):
                self[k] = v

    """for reordering in non alphabetical order"""
    def __repr__(self):
        return json.dumps(OrderedDict(self), ensure_ascii=False)


class ScrapperassignmentItem(OrderedItem):
    date_published = scrapy.Field()
    title = scrapy.Field()
    detail = scrapy.Field()
    news_from = scrapy.Field()
    url = scrapy.Field()
