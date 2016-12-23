import json

with open("./../data/new_team_pace.json") as fp:
    data = json.load(fp)

result = dict()
for teams , years in data.items():
    for name in teams.split("@"):
        result[name] = data[teams]

with open("./../data/clean_team_pace.json" , 'wb') as fp:
    json.dump(result , fp)
