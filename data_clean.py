import json
import os
import numpy as np
import pandas
import time
import datetime

def str2mins(string):
    x = time.strptime(string,'%M:%S')
    return datetime.timedelta(minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

def str2float(num):
    try:
        return float(num)
    except:
        return -1

data_path = "./../origin_data/"

datas = dict()
for dirs , root , files in os.walk(data_path):
    for filename in files:
        f = open(data_path + filename , "rb")
        data = json.load(f)
        datas.update(data)


count = 0
for date , games in datas.items():
    for game , teams in games.items():
        for team , players in teams.items():
            for player , numbers in players.items():
                if len(numbers) == 2:
                    del datas[date][game][team][player]
                    continue
                numbers_dict = dict()
                length = len(numbers)
                numbers_dict["DRtg"] = str2float(numbers.pop())
                numbers_dict["ORtg"] = str2float(numbers.pop())
                numbers_dict["USG%"] = str2float(numbers.pop())
                numbers_dict["TOV%"] = str2float(numbers.pop())
                numbers_dict["BLK%"] = str2float(numbers.pop())
                numbers_dict["STL%"] = str2float(numbers.pop())
                numbers_dict["AST%"] = str2float(numbers.pop())
                numbers_dict["TRB%"] = str2float(numbers.pop())
                numbers_dict["DRB%"] = str2float(numbers.pop())
                numbers_dict["ORB%"] = str2float(numbers.pop())
                numbers_dict["FTr"] = str2float(numbers.pop())
                numbers_dict["3PAr"] = str2float(numbers.pop())
                numbers_dict["eFG%"] = str2float(numbers.pop())
                numbers_dict["TS%"] = str2float(numbers.pop())
                numbers_dict["MP"] = numbers.pop()
                if length == 35:
                    numbers_dict["+/-"] = str2float(numbers.pop())
                numbers_dict["PTS"] = str2float(numbers.pop())
                numbers_dict["PF"] = str2float(numbers.pop())
                numbers_dict["TOV"] = str2float(numbers.pop())
                numbers_dict["BLK"] = str2float(numbers.pop())
                numbers_dict["STL"] = str2float(numbers.pop())
                numbers_dict["AST"] = str2float(numbers.pop())
                numbers_dict["TRB"] = str2float(numbers.pop())
                numbers_dict["DRB"] = str2float(numbers.pop())
                numbers_dict["ORB"] = str2float(numbers.pop())
                numbers_dict["FT%"] = str2float(numbers.pop())
                numbers_dict["FTA"] = str2float(numbers.pop())
                numbers_dict["FT"] = str2float(numbers.pop())
                numbers_dict["3P%"] = str2float(numbers.pop())
                numbers_dict["3PA"] = str2float(numbers.pop())
                numbers_dict["3P"] = str2float(numbers.pop())
                numbers_dict["FG%"] = str2float(numbers.pop())
                numbers_dict["FGA"] = str2float(numbers.pop())
                numbers_dict["FG"] = str2float(numbers.pop())
                numbers_dict["MP"] = numbers.pop()
                
                datas[date][game][team][player] = numbers_dict
                if len(numbers) != 0:
                    print "error"

with open('total_data.json', 'w') as fp:
    json.dump(datas, fp) 
