from bs4 import BeautifulSoup
from urllib import urlopen
import json
#fetch players list from site

url = "http://fantasy.premierleague.com/player-list/"
html = urlopen(url).read()


soup = BeautifulSoup(html)
h2s = soup.select("h2")
tables = soup.select("table")

first = True
title =""
players = []
for i,table in enumerate(tables):
    if first:
         title =  h2s[int(i/2)].text
    for tr in table.select("tr"):
        player = (title,)
        for td in tr.select("td"):
            player = player + (td.text,)
        if len(player) > 1:
            players.append(player)

    first = not first
players_per_club = {}

for i in players:
	position, player, club, price ,point = i
	players_per_club.setdefault(club.encode('ascii','ignore'), []).append(player.encode('ascii','ignore'))
print players_per_club
with open('allplayers.html','w') as  fh:
	fh.write(str(players_per_club))
