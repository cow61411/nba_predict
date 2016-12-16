import pandas as pd
import json

data = pd.read_csv("./../data/league_average.csv" , index_col = 'year')

result = dict()

for i in range(2007 , 2017):
    temp = dict()
    temp["MP"] = float(data.MP[i])
    temp["FG"] = float(data.FG[i])
    temp["FGA"] = float(data.FGA[i])
    temp["FT"] = float(data.FT[i])
    temp["FTA"] = float(data.FTA[i])
    temp["ORB"] = float(data.ORB[i])
    temp["TRB"] = float(data.TRB[i])
    temp["AST"] = float(data.AST[i])
    temp["TOV"] = float(data.TOV[i])
    temp["PF"] = float(data.PF[i])
    temp["PTS"] = float(data.PTS[i])
    temp["Pace"] = float(data.Pace[i])
    result[i] = temp

with open("./../data/league_average.json" , "wb") as fp:
    json.dump(result , fp)
