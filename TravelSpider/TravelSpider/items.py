# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TravelspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LowpriceItem(scrapy.Item):
    cityName = scrapy.Field()
    arrCityCode = scrapy.Field()
    airportLatitude = scrapy.Field()
    airportLongitude = scrapy.Field()
    price = scrapy.Field()
    