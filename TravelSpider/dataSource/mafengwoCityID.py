import urllib.request
import urllib.parse
import json
import os

base_url = "http://www.mafengwo.cn/ajax/router.php?sAct=KMdd_StructWebAjax|SearchMdd&sName="
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
}
with open('allAirport.json','r',encoding="utf-8") as f:
    airPort = json.loads(f.read())
    items = []
    for city in airPort:
        url = base_url + urllib.parse.quote(city['cityName'])  
        print (city['cityName']) 
        request = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(request).read()
        results = json.loads(response)
        cityList = results['data']['mdd']
        if len(cityList) == 0:
            city['cityID'] = 000000000000000000000000000000000
        elif len(cityList) == 1 :
            city['cityID'] = cityList[0]['mddid']
        else:
            mddid = []
            for i in cityList:
                if i['mdd_num'] == 3:
                    mddid.append(i['mddid'])
            if len(mddid) == 1:
                city['cityID'] = mddid[0]
            else:
                city['cityID'] = 11111111111111111111111111111111111
        items.append(city)

    with open('allAirport_V2.json','w',encoding='utf-8') as f:
        f.write(json.dumps(items,ensure_ascii=False))
        f.close()
        