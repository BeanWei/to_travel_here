import os
import json

with open(os.path.abspath(os.path.dirname(__file__))+'/1.txt',encoding='utf-8') as f:
    file = f.readlines()
results = []
index = 0
while index <= 661 :
    result = {}
    result['provinces'] = file[index].strip('\n')      
    result['airportShortName'] = file[index+1].strip('\n')              
    result['cityName'] = file[index+2].strip('\n')    
    result['cityNameEN'] = file[index+3].strip('\n')    
    result['airportName'] = file[index+4].strip('\n')    
    results.append(result)
    index = index+5
new_file = open(os.path.abspath(os.path.dirname(__file__))+'/allAirport.json','w',encoding='utf-8')
json.dump(results,new_file,ensure_ascii=False)
new_file.close()