import os
import scrapy
from scrapy import Request
from scrapy import log
import json 

cityID = 10444

class GetAttractionsSpider(scrapy.Spider):
    name = 'getAttractions'
    allowed_domains = ['http://www.mafengwo.cn/']

    '''
    排序方式：最新问题（type=0）
    景点(游玩地方推荐)：http://www.mafengwo.cn/qa/ajax_qa/more?type=0&mddid=10444&tid=1293&sort=1&key=&page=0
    行程(游玩路线推荐)：http://www.mafengwo.cn/qa/ajax_qa/more?type=0&mddid=10444&tid=1294&sort=1&key=&page=0
    住宿(住宿地点推荐)：http://www.mafengwo.cn/qa/ajax_qa/more?type=0&mddid=10444&tid=1291&sort=1&key=&page=0
    '''

    def start_requests(self):
        baseUrl = [
            "http://www.mafengwo.cn/qa/ajax_qa/more?type=0&mddid=10444&tid=1293&sort=1&key=&page=",
            "http://www.mafengwo.cn/qa/ajax_qa/more?type=0&mddid=10444&tid=1294&sort=1&key=&page=",
            "http://www.mafengwo.cn/qa/ajax_qa/more?type=0&mddid=10444&tid=1291&sort=1&key=&page="
        ]
        page_index = 0
        for suburl in baseUrl:
            url = suburl + page_index
            page_index += 1
            yield Request(url=url,callback=self.parse)

    def parse(self,response):
        result = json.loads(response.body)
        