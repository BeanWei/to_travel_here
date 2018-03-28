import scrapy
import json
from scrapy import Request
import re
import urllib.request
from TravelSpider.items import AllHotelItem

cityID = 10444

class GetallHotel(scrapy.Spider):
    name = "getAllHotel"
    custom_settings = {
        'ITEM_PIPELINES' : {
            'TravelSpider.pipelines.JsonExporterPipeline_Four': 300,
        }      
    }

    def start_requests(self):
        noUrl = "http://www.mafengwo.cn/hotel/ajax.php?iMddId=%s&iPage=1&sAction=getPoiList5" % cityID
        total_page = round(((json.loads(urllib.request.urlopen(noUrl).read()))['msg']['count'])//20)
        for ipage in range(1,int(total_page)+1):
            url = "http://www.mafengwo.cn/hotel/ajax.php?iMddId=%s&iPage=%s&sAction=getPoiList5" % (cityID,ipage)
            yield Request(url=url,callback=self.parse)

    def parse(self,response):
        item = AllHotelItem()
        item['cityID'] = cityID
        #data-name=\"锦江之星（青岛中山路店）\"
        hotels = ','.join(re.findall(r'data-name="(.*?)"',(json.loads(response.body))['html']))
        item['hotelName'] = hotels.replace(' ','')
        yield item
