import matplotlib.pyplot as plt
import json
import datetime

f = open("./../data/time_serial_detail_data.json" , 'rb')
test = json.load(f)

name = ""
max_num = 0
'''
for player , games in test.items():
    if len(games) > max_num:
        name = player
        max_num = len(games)
'''

time = list()
per = list()

for date , number in test["Paul Millsap"].items():
    time.append(date)
    per.append(number["PER"])


data = sorted(zip(time , per) , key = lambda x : x[0] , reverse = True)

#time = map(lambda x : x[0] , data)
#per = map(lambda x : x[1] , data)

temp = dict()
for time , per in data:
    year = int(time[:4])
    if year not in temp:
        temp[year] = 

print time[0]
plt.plot(time,per)
plt.show()


    

