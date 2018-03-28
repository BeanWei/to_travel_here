import telnetlib
import os
import urllib.request
import json

path = os.path.abspath(os.path.dirname(__file__))

def checkIP():
    file = open(path+'/ProxyPools.txt')
    output = open(path+'/okIP.txt','a+')
    ok = []
    for line in file.readlines():
        print (line)
        try:
            i = line.split(':')
            host = i[0]
            port = i[1]
            telnetlib.Telnet()
            try:
                telnetlib.Telnet('127.0.0.1', port='80', timeout=20)
            except:
                print ('connect failed')
            else:
                print ('success')
                ok.append(line)
        except:
            continue
    for ip in ok:
        output.write(ip+'\n')
    print ("it's OK")

def getIP():
    file = open(path+'/ProxyPools.txt',"a+")
    for page in range(1,8):
        url = "http://ip.jiangxianli.com/api/proxy_ips?page=" + str(page)
        data = json.loads(urllib.request.urlopen(url).read())
        for ip in data['data']['data']:
            file.write(ip['ip']+":"+ip['port']+"\n")
    file.close()

