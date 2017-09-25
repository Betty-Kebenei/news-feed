import urllib
import json

def get_data():
    
    url='http://34.207.10.230:3000/posts'
    req=urllib.urlopen(url)
    data=req.read().decode('utf')
    json_parse=json.loads(data)
    for i in json_parse:
        print i     

get_data()