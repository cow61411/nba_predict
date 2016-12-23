import json

with open("./../data/name_cleaned_data.json" , 'rb') as fp:
    data = json.load(fp)

result = dict()

key = 1
minn = 99

for date , games in data.items():
    for game , teams in games.items():
        for team , players in teams.items():
            for player , _ in players.items():
                if player not in result:
                    result[player] = key
                    key += 1


with open("./../data/player_dict.json" , "wb") as fp:
    json.dump(result , fp)
