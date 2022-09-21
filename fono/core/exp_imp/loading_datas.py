import json

file = "ISRC_SOCIEDADE.json"
with open(file, "r") as f:
    data = json.load(f)

print(data)
for soc in data['sociedades']:
      print(soc)

