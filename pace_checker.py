import json

with open("./../data/team_pace.json" , 'rb') as fp:
    data = json.load(fp)

for team , years in data.items():
    print team , len(years)
