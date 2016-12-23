import json
import numpy as np
import datetime
import pandas as pd

name = "Paul Millsap"

with open("./../data/player_monthly_PER.json") as fp:
    data = json.load(fp)


date = list()
pers = list()

mt = range(1 , 13)
mt = map(lambda x : "%02d" % x , mt)

yt = range(2006 , 2017)
yt = map(str , yt)

result = dict()
for year in yt:
    for month in mt:
        #date.append(year + "-" + month)
        #pers.append(data[name][year][month]["PER"])
        if data[name][year][month]["PER"] == "NAN":
            result[year + "-" + month] = "NaN"
        else:
            result[year + "-" + month] = data[name][year][month]["PER"]

df = pd.DataFrame(result.items(), columns=['month', '#Passengers'] , index = result.keys())
df.to_csv("test.csv")

