import json

with open("./../../data/team_rating.json" , "rb") as fp:
    data = json.load(fp)

for team , years in data.items():
    print years.keys()
