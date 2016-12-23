import requests
import re
from bs4 import BeautifulSoup

url = "http://www.basketball-reference.com/leagues/NBA_2016.html"

res = requests.get(url)
temp = res.text.replace("<!--" , "")
temp = temp.replace("-->" , "")
soup = BeautifulSoup(temp , "html.parser")


for a in soup.find_all('div' , class_ = "table_outer_container"):
    print a.text
