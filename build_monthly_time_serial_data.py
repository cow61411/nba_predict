import json

with open("./../data/time_serial_detail_data.json" , 'rb') as fp:
    data = json.load(fp)

m_nu = range(1 , 13)
m_nu = map(lambda x : "%02d" % x , m_nu)

y_nu = range(2006 , 2017)
y_nu = map(lambda x : str(x) , y_nu)

result = dict()
for player , dates in data.items():
    temp = dict()
    for y in y_nu:
        m_temp = dict()
        for m in m_nu:
            nu_temp = dict()
            nu_temp["PER"] = 0
            nu_temp["count"] = 0
            m_temp[m] = nu_temp
        temp[y] = m_temp
    for date , numbers in dates.items():
        year = date[:4]
        month = date[4:6]
        temp[year][month]["PER"] += numbers["PER"]
        temp[year][month]["count"] += 1

    for year , months in temp.items():
        for month , nums in months.items():
            if nums["count"] == 0:
                #temp[year][month]["PER"] = "NaN"
                #del temp[year][month]["count"]
                del temp[year][month]
            else:
                temp[year][month]["PER"] /= float(nums["count"])
                del temp[year][month]["count"]
    result[player] =  temp

with open("./../data/player_monthly_PER.json" , 'wb') as fp:
    json.dump(result , fp)

        
