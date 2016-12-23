import numpy as np
from sklearn import linear_model

def get_predict_PER(name , time_data , target):
    input_time = list()
    input_PER = list()
    if name in time_data:
        for year , months in time_data[name].items():
            for month , nums in months.items():
                input_time.append([12 * (int(year) - 2005) + int(month)])
                input_PER.append([nums["PER"]])
                reg = linear_model.LinearRegression(normalize = True)
                reg.fit(input_time , input_PER)
                return reg.predict([target])[0]
    else:
        return None

