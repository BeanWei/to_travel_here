# -*- coding: utf-8 -*-
import os
import scrapy
from scrapy import Request
from scrapy import log
import json

from TravelSpider.items import LowpriceItem

depCityCode = 'CKG'
leaveDate = '2018-04-05'
backDate = '2018-04-08'

class GetairportlowpriceSpider(scrapy.Spider):
    name = 'getAirportLowprice'
    custom_settings = {
        'ITEM_PIPELINES' : {
            'TravelSpider.pipelines.JsonExporterPipeline_One': 300,
        }      
    }
    allowed_domains = ['https://www.alitrip.com/']

    def start_requests(self):
        with open(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../.."))+'/dataSource/allAirport.json','r',encoding="UTF-8") as f:
            temp = json.loads(f.read())
        for arrCity in temp:
            item = LowpriceItem()
            item['cityName'] = arrCity['cityName']
            item['airportName'] = arrCity['airportName']
            arrCityCode = arrCity['airportShortName']
            startUrl = "https://r.fliggy.com/cheapestCalendar/pc?bizType=0&tripType=1&depCityCode=%s&arrCityCode=%s&leaveDate=%s&backDate=%s&nDays=7&calendarType=0&agentId=" % (depCityCode,arrCityCode,leaveDate,backDate)            
            item['arrCityCode'] = arrCityCode
            yield Request(url=startUrl,meta={'item_1':item},callback=self.parse)

    def parse(self,response):
        item = response.meta['item_1']
        results = json.loads(response.body)
        if results['success']:
            for result in results['result']:
                if result['leaveDate'] == leaveDate and result['backDate'] == backDate and result['price'] != 0:
                    item['price'] = result['price']
                    yield item
        else:
            log.msg("获取低价的URL解析失败")
            
