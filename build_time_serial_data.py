import json

with open("./../data/player_dict.json") as fp:
    player_dict = json.load(fp)

with open("./../data/player_data_with_per.json") as fp:
    game_detail = json.load(fp)

result = dict()
for name , _ in player_dict.items():
    temp = dict()
    for date , games in game_detail.items():
        for game , teams in games.items():
            for team , players in teams.items():
                for player , numbers in players.items():
                    if player == name and player != "Team Totals":
                        temp[date] = numbers
    result[name] = temp

with open("./../data/time_serial_detail_data.json" , 'wb') as fp:
    json.dump(result , fp)


