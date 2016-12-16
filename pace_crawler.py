from bs4 import BeautifulSoup
import requests
import json

url = "http://www.basketball-reference.com/teams/%s/%d.html"

years = range(2007 , 2017)

team = {"Toronto Raptors" : "TOR" , 
        "New York Knicks" : "NYK" ,
        "Seattle SuperSonics" : "SEA",
        "Boston Celtics" : "BOS",
        "Brooklyn Nets" : "BRK",
        "New Jersey Nets" : "NJN",
        "Philadelphia 76ers" : "PHI",
        "Charlotte Hornets" : "CHO",
        "Charlotte Bobcats" : "CHA",
        "Atlanta Hawks" : "ATL",
        "Washington Wizards" : "WAS",
        "Orlando Magic" : "ORL",
        "Miami Heat" : "MIA",
        "Cleveland Cavaliers" : "CLE",
        "Chicago Bulls" : "CHI",
        "Detroit Pistons" : "DET",
        "Indiana Pacers" : "IND",
        "Milwaukee Bucks" : "MIL",
        "Utah Jazz" : "UTA",
        "Oklahoma City Thunder" : "OKC",
        "Portland Trail Blazers" : "POR",
        "Denver Nuggets" : "DEN",
        "Minnesota Timberwolves" : "MIN",
        "San Antonio Spurs" : "SAS",
        "Houston Rockets" : "HOU",
        "Memphis Grizzlies" : "MEM",
        "New Orleans Pelicans" : "NOP",
        "Dallas Mavericks" : "DAL",
        "Golden State Warriors" : "GSW",
        "Los Angeles Clippers" : "LAC",
        "Sacramento Kings" : "SAC",
        "Los Angeles Lakers" : "LAL",
        "Phoenix Suns" : "PHO",
        "New Orleans Hornets" : "NOH"}

result = {}

for name , short in team.items():
    temp = dict()
    for year in years:
        res = requests.get(url % (short , year))
        soup = BeautifulSoup(res.text , "html.parser")

        for a in soup.find_all("a" , href = True , text = "Pace"):
            target = a.parent.parent.get_text()
            target = target[target.index("Pace"):]
            target = target[target.index(":") + 1:target.find("(")]
            target = float(target)
            temp[year] = target
    name = name.replace(" " , "")
    name = name.lower()
    result[name] = temp

with open("./../data/team_pace.json" , "wb") as fp:
    json.dump(result , fp)
