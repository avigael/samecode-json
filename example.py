import json

f = open('samecode.json')

data = json.load(f)

location = data["001011"]
print(location["city"] + ", " + location["state"])

f.close()