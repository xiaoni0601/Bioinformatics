import urllib2
import json

locu_api = 'xxxxxxxxxxx'
def locu_search(query):
    api_key = locu_api
    url = 'https:api....' + api_key
    locality = query.replace('', '%20')
    final_url = url + "&locality" + locality + "&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.loads(json_obj)
    
    for item in data['objects']:
        print(item['name'], item['phone'])