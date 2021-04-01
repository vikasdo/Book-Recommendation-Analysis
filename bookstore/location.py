import requests
import json

def get_location():

    url = "http://api.ipstack.com/check?access_key=d9eba6935958a1c03d2af3ffab801887"


    response = requests.request("GET", url)
    # print(response.text)
    response = json.loads(response.text)
    ip = response["ip"]
    city = response["city"]
    lat = response["latitude"]
    lon = response["longitude"]
    country = response["country_name"]
    result = city+','+country + ',' + str(lat)+','+str(lon)
    return result

# print(get_location())

