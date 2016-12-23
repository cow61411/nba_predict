import json

with open("./../data/player_data_with_per.json" , 'rb')as fp:
    data = json.load(fp)

for date , games in data.items():
    for game , teams in games.items():
        for team , players in teams.items():
            for player , numbers in players.items():
                #print numbers.keys()
                EFF = (numbers["PTS"] + numbers["TRB"] + numbers["AST"] + numbers["STL"] + numbers["BLK"]) - (numbers["FGA"] - numbers["FG"]) - (numbers["FTA"] - numbers["FT"]) - numbers["TOV"]

                GmSc = numbers["PTS"] + 0.4 * numbers["FG"] - 0.7 * numbers["FGA"] - 0.4 * (numbers["FTA"] - numbers["FT"]) + 0.7 * numbers["ORB"] + 0.3 * numbers["DRB"] + numbers["STL"] + 0.7 * numbers["AST"] + 0.7 * numbers["BLK"] - 0.4 * numbers["PF"] - numbers["TOV"]

                data[date][game][team][player]["EFF"] = EFF
                data[date][game][team][player]["GmSc"] = GmSc

with open("./../data/player_data_with_per_eff_gmsc.json" , 'wb') as fp:
    json.dump(data , fp)


