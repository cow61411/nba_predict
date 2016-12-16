import json
import numpy as np
import os
#import sklearn

def str2mins(string):
    x = time.strptime(string,'%M:%S')
    return datetime.timedelta(minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

with open("./../data/total_data.json" , 'rb') as fp:
    datas = json.load(fp)
temp = dict()
for date , games in datas.items():
    date_num = int(date)
    temp[date_num] = games
datas = temp

for date , games in datas.items():
    temp = dict()
    for game , teams in games.items():
        game = game[:game.index("Box")]
        game = game.replace(" at " , "/")
        game = game.replace(" " , '')
        game = game.lower()
        temp[game] = teams
    datas[date] = temp

for date , games in datas.items():
    for game , teams in games.items():
        temp = dict()
        for team , players in teams.items():
            team = team[:team.index("(")]
            team = team.replace(" " , '')
            team = team.lower()
            temp[team] = players
        datas[date][game] = temp

del datas[20141113]["sacramentokings/memphisgrizzlies"]["sacramentokings"]["Ryan Hollins"]

for date , games in datas.items():
    for game , teams in games.items():
        for team , players in teams.items():
            for player , numbers in players.items():
                time = numbers["MP"]
                if time.find(":") != -1:
                    mins = float(time[:time.index(":")])
                    sec = float(time[time.index(":") + 1:]) / 60.0
                    time = mins + sec
                else:
                    time = float(time)
                datas[date][game][team][player]["MP"] = time



with open("name_cleaned_data.json" , 'wb') as fp:
    json.dump(datas , fp)

