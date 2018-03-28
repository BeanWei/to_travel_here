import scrapy
import json
from scrapy import FormRequest
import re
from TravelSpider.items import AllViewsetItem

cityID = 10444

url = "http://www.mafengwo.cn/ajax/router.php"

class GetAllViewsetSpider(scrapy.Spider):
    name = "getAllViewset"
    custom_settings = {
        'ITEM_PIPELINES' : {
            'TravelSpider.pipelines.JsonExporterPipeline_Three': 300,
        }      
    }
    allowed_domains = ['www.mafengwo.cn']

    def start_requests(self):
        post_data = {
            'sAct': 'KMdd_StructWebAjax|GetPoisByTag',
            'iMddid': str(cityID),
            'iTagId': '0',
            'iPage': '1'
        }
        yield FormRequest(url=url,formdata=post_data,callback=self.parse_totalPage)

    def parse_totalPage(self,response):
        total_page = re.findall(r'<span class="count">共<span>(.*?)</span>页',(json.loads(response.body))['data']['page'])[0]
        for ipage in range(1,int(total_page)+1):
            post_data = {
            'sAct': 'KMdd_StructWebAjax|GetPoisByTag',
            'iMddid': str(cityID),
            'iTagId': '0',
            'iPage': str(ipage)
            }
            yield FormRequest(url=url,formdata=post_data,callback=self.parse_detail)

    def parse_detail(self,response):
        viewsets = ','.join(re.findall(r'<h3>(.*?)</h3>',(json.loads(response.body))['data']['list']))
        item = AllViewsetItem()
        item['cityID'] = cityID
        item['viewsetName'] = viewsets
        yield item