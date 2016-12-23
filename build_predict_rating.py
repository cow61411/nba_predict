from sklearn import linear_model
import json

with open("./../../data/team_rating.json" , "rb") as fp:
    data = json.load(fp)

result = dict()
for team , years in data.items():
    temp_dict = dict()
    reg_ORtg = linear_model.LinearRegression()
    reg_DRtg = linear_model.LinearRegression()
    year_input = list()
    ORtg_input = list()
    DRtg_input = list()
    for year , nums in years.items():
        year_input.append([int(year) - 2005])
        ORtg_input.append([float(nums["ORtg"])])
        DRtg_input.append([float(nums["DRtg"])])
    reg_ORtg.fit(year_input , ORtg_input)
    predict_ORtg = reg_ORtg.predict([[12]])
    reg_DRtg.fit(year_input , DRtg_input)
    predict_DRtg = reg_DRtg.predict([[12]])
    temp_dict["ORtg"] = predict_ORtg[0][0]
    temp_dict["DRtg"] = predict_DRtg[0][0]
    result[team] = temp_dict

with open("./../../data/predict_rating.json" , "wb") as fp:
    json.dump(result , fp)
