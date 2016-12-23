import os
import json
import pandas as pd

with open("./../../data/new_team_pace.json" , "rb") as fp:
    team_pace = json.load(fp)

data_path = "./../../data/rating/"

year_dict = dict()
for dirs , root , files in os.walk(data_path):
    for filename in files:
        temp_dict = dict()
        data = pd.read_csv(data_path + filename , index_col = "Rk")
        year = int(filename[:-4])
        for i in range(1 , 31):
            inner_temp_dict = dict()
            inner_temp_dict["ORtg"] = data.ORtg[i]
            inner_temp_dict["DRtg"] = data.DRtg[i]
            team_name = data.Team[i]
            team_name = team_name.replace(" " , "")
            team_name = team_name.lower()
            if team_name.endswith("*"):
                team_name = team_name[:-1]
            temp_dict[team_name] = inner_temp_dict
        year_dict[year] = temp_dict

result = dict()
for teams , _ in team_pace.items():
    names =  teams.split("@")
    temp_dict = dict()
    for i in range(2005 , 2016):
        for t_name , nums in year_dict[i].items():
            if t_name in names:
                temp_dict[i] = year_dict[i][t_name]
    result[teams] = temp_dict

total_result = dict()
for teams , years in result.items():
    for team in teams.split("@"):
        total_result[team] = result[teams]
        
with open("./../../data/team_rating.json" , "wb") as fp:
    json.dump(total_result , fp)

