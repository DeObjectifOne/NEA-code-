import requests
import json

response = requests.get(
    "https://api-server.dataquest.io/economic_data/countries")
data = response.json()
print(response.json())


def jprint(obj):
  text = json.dumps(obj, sort_keys=True, indent=4)
  print(text)


jprint(response.json())
