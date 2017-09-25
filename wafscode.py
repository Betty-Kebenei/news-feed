from urllib.request import urlopen
import json

def get_data():

    country = input("Search Country: ")
    url='https://restcountries.eu/rest/v2/name/'+country+'?fullText=true'
    req=urlopen(url)
    data=req.read().decode('utf')
    json_parse=json.loads(data)[0]
    Region = json_parse["region"]
    capital = json_parse["capital"]
    population = json_parse["population"]
    

    print((country,Region,population,capital))

get_data()