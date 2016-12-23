import json

with open("./../data/name_cleaned_data.json" , 'rb') as fp:
    data = json.load(fp)

result = dict()

key = 1

for date , games in data.items():
    for game , teams in games.items():
        for team , players in teams.items():
            if team not in result:
                result[team] = key
                key += 1


with open("./../data/team_dict.json" , "wb") as fp:
    json.dump(result , fp)
