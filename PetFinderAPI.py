import requests
import json
from pprint import pprint

key = "8bfef23cb32e0eacfc202410785b3ef6"
url = "http://api.petfinder.com/shelter.find?" \
      "location=19123&" \
      "format=json&" \
      "count=100&" \
      "key=" + key
r = requests.get(url)
json_data = json.loads(r.text)

shelters = json_data['petfinder']['shelters']['shelter']
shelters_with_data = []


for shelter in shelters:
    if len(shelter['address1']) > 0:
        address = shelter['address1']['$t']
    else: address = ''
    city = shelter['city']['$t']
    email = shelter['email']['$t']
    id = shelter['id']['$t']
    latitude = shelter['latitude']['$t']
    longitude = shelter['longitude']['$t']
    name = shelter['name']['$t']
    if len(shelter['phone']) > 0:
        phone = shelter['phone']['$t']
    else: phone = ''
    state  = shelter['state']['$t']
    zipcode = shelter['zip']['$t']

    shelter_data = [id, name, email, phone, address, city, state, zipcode, latitude, longitude]
    shelters_with_data.append(shelter_data)
    # print(shelter_data)

for shelter in shelters_with_data[:1]:
    id = shelter[0]
    # print(id)

    key = "8bfef23cb32e0eacfc202410785b3ef6"
    url = "http://api.petfinder.com/shelter.getPets?" \
          "id=" + id + '&' \
          "format=json&" \
          "key=" + key
    r = requests.get(url)
    json_data = json.loads(r.text)

    # print(json_data)
    pets = json_data['petfinder']['pets']['pet']
    pprint(pets)
    pets_with_data = []

    for pet in pets:
        pass