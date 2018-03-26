import urllib.request
import json
import os

url = "https://www.cn.kayak.com/s/horizon/exploreapi?airport=CKG&v=1&initLoad=false"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'cookie': 'Apache=K$yVIw-AAABYl$FDPI-a2-NNniTQ; kykprf=351; kayak=3on7VS8MMvag_XNYX8g5; vid=157a8e10-308f-11e8-81a2-03e8bf1a83bd; _pxvid=157a8e10-308f-11e8-81a2-03e8bf1a83bd; Hm_lvt_6e019bdf64b0b0b9fe019986c76c056b=1522025176; __gads=ID=cf43700eefe390f0:T=1522025189:S=ALNI_MbZydGhQ8FUPqGRUWhHV4RbyVSGRQ; _sctr=1|1521993600000; _scid=8dbf7a90-91b9-483a-bf80-10bd2d5e6a87; cluster=5; p1.med.sid=H-5VS$vN$_j6tmHYDpUooXs-RzAavxHxKC1VHbNqHteQBVGLWtTKTMKgta56TyBZN; p1.med.token=2KVHY1dPpnglohUIMwLewA; NSC_q5-tqbslmf=ffffffff09892a7045525d5f4f58455e445a4a422a59; p1.med.sc=1; NSC_q5-lbqj=ffffffff0989be4145525d5f4f58455e445a4a42299c; _ga=GA1.3.2007294695.1522029328; _gid=GA1.3.1919831749.1522029328; Hm_lpvt_6e019bdf64b0b0b9fe019986c76c056b=1522029439; _px2=eyJ1IjoiMDNhOTgxNTAtMzA5OS0xMWU4LTk4YzItMjNmZjlhMjc1NDkxIiwidiI6IjE1N2E4ZTEwLTMwOGYtMTFlOC04MWEyLTAzZThiZjFhODNiZCIsInQiOjE1MjIwMjk3Mzc2NjIsImgiOiIxNWMyMzMzODM5MjZmMzY4OTcyN2UyMjlkMDQ5MTRlOTM3YjFiZDc4MzNlZmE5ZTM0OTMwMjc3YzlkNGJmNTc1In0='
}
            

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request).read()
results = json.loads(response)
items = []
for place in results["destinations"]:
    item = {}
    item['country'] = place['country']['name']
    item['cityID'] = place['city']['id']
    item['cityName'] = place['city']['name']
    item['airportLatitude'] = place['airport']['latitude']
    item['airportLongitude'] = place['airport']['longitude']
    item['airportShortName'] = place['airport']['shortName']
    items.append(item)
file = open(os.getcwd()+'/allAirport.json','w',encoding='utf-8')
json.dump(items,file,ensure_ascii=False)
file.close()