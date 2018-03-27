import os
import scrapy
from scrapy import Request
from scrapy import log
import json 
import re
from scrapy import log

from TravelSpider.items import AllUsefulInfoItem

cityID = 10444

class GetAllUsefulInfoSpider(scrapy.Spider):
    name = 'getAllUsefulInfo'
    custom_settings = {
        'ITEM_PIPELINES' : {
            'TravelSpider.pipelines.JsonExporterPipeline_Two': 300,
        }      
    }
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
            item = AllUsefulInfoItem()
            url = suburl + str(page_index)
            page_index += 1
            item['cityID'] = cityID
            if "tid=1293" in suburl:
                item['tid'] = "景点"
            elif "tid=1294" in suburl:
                item['tid'] = "行程"
            elif "tid=1291" in suburl:
                item['tid'] = "住宿"
            else:
                log.msg("初始化URL生成错误")
            yield Request(url=url,meta={'item_1':item},callback=self.parse)

    def parse(self,response):
        item = response.meta['item_1']
        result = json.loads(response.body)
        if result['data']['html'] != '':
            wendaSuburl = re.findall(r'href="/wenda/detail-(.*?).html"',result['data']['html'])
            for suburl in wendaSuburl:
                wendaUrl = "http://www.mafengwo.cn/wenda/detail-%s.html" % str(suburl)
                print (wendaUrl)
                yield Request(url=wendaUrl,meta={'item_1':item},callback=self.parse_wenda)
            
    def parse_wenda(self,response):
        item = response.meta['item_1']
        answers = "".join(response.xpath('//div[@class=""]//text()').extract())
        item['answers'] = answers
        yield item