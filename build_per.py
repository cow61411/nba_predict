import json
import pandas as pd

with open("./../data/league_average.json" , 'rb') as fp:
    league_average = json.load(fp)

with open("./../data/team_pace.json" , 'rb') as fp:
    team_pace = json.load(fp)

with open("./../data/name_cleaned_data.json" , 'rb') as fp:
    player_data = json.load(fp)

lg_aPER = {2006: 12.29 , 2007 : 12.38 , 2008 : 12.41 , 2009 : 12.85 , 2010 : 12.76 , 2011 : 12.41 , 2012 : 12.77 , 2013 : 12.37 , 2014 : 12.43 , 2015 : 12.61 , 2016 : 12.83}

for date , games in player_data.items():
    for game , teams in games.items():
        for team , players in teams.items():
            for player , numbers in players.items():
                if numbers["MP"] == 0:
                    continue

                td = player_data[date][game][team]["Team Totals"] # team data
                year = date[:4]
                lg = league_average[year] #league average data
                try:
                    tp = team_pace[team][year] # team pace
                except:
                    print team , year

                factor = (2 / 3.0) - (0.5 * (lg["AST"] / lg["FG"])) / (2 * (lg["FG"] / lg["FT"]))
                VOP = lg["PTS"] / (lg["FGA"] - lg["ORB"] + lg["TOV"] + 0.44 * lg["FTA"])
                DRB_perc = (lg["TRB"] - lg["ORB"]) / lg["TRB"]

                uPER = (1 / numbers["MP"]) \
                    * (numbers["3P"] \
                    + (2 / 3.0) * numbers["AST"] \
                    + (2 - factor * (td["AST"] / td["FG"])) * numbers["FG"]\
                    + (numbers["FT"] * 0.5 * (1 + (1 - (td["AST"] / td["FG"])) + (2 / 3.0) * (td["AST"] / td["FG"])))\
                    - VOP * numbers["TOV"]\
                    - VOP * DRB_perc * (numbers["FGA"] - numbers["FG"])\
                    - VOP * 0.44 * (0.44 + (0.56 * DRB_perc)) * (numbers["FTA"] - numbers["FT"])\
                    + VOP * (1 - DRB_perc) * (numbers["TRB"] - numbers["ORB"])\
                    + VOP * DRB_perc * numbers["ORB"]\
                    + VOP * numbers["STL"]\
                    + VOP * DRB_perc * numbers["BLK"]\
                    - numbers["PF"] * ((lg["FT"] / lg["PF"]) - 0.44 * (lg["FTA"] / lg["PF"]) * VOP))

                pace_adj = lg["Pace"] / tp

                aPER = pace_adj * uPER

                PER = aPER * (15 / lg_aPER[int(year)])
                
                player_data[date][game][team][player]["PER"] = PER

