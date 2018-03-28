import json
import os

'''
with open(os.path.abspath(os.path.join(os.getcwd(), ".."))+'/AllViewset.json','r',encoding='utf-8') as f:
    viewsets = json.loads(f.read())
    cityID = viewsets[0]['cityID']
    file = open(str(cityID)+'.txt','a+',encoding='utf-8')
    for viewset in viewsets:
        lines = viewset['viewsetName'].split(',')
        for line in lines:
            file.write(line+' '+'ns'+'\n')
    file.close()
'''
with open(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'/AllHotel.json','r',encoding='utf-8') as f:
    viewsets = json.loads(f.read())
    cityID = viewsets[0]['cityID']
    file = open(str(cityID)+'_hotel.txt','a+',encoding='utf-8')
    for viewset in viewsets:
        lines = viewset['hotelName'].split(',')
        for line in lines:
            file.write(line+' '+'ns'+'\n')
    file.close()