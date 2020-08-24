import requests
import json

baseURL = "https://cartocdn-gusc-c.global.ssl.fastly.net/dhhs/api/v1/map/dhhs@fc1c7adf@4b5a953f5b4fe87521c15fa609d5e1b1:1598241218631/1/attributes/"

initialValue = 1

start = 1
end = 10
aggregate = {}


for x in range (start, end):
  r = requests.get(baseURL + str(x))
  if (r.status_code == 200):
    aggregate[x] = json.loads(r.text)

print(aggregate)
