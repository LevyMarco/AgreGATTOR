#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

#Getting RSS
foo = "https://caruaru.upe.br/feed/"
bar = requests.get(foo)
bar.raise_for_status() #Debugger

foobar = BeautifulSoup(bar.text, "xml")
#print(foobar)
quux = foobar.find_all("item")

print(quux[0].pubDate.text, "\n")
print(quux[0].title.text, "\n")
print(quux[0].description.text, "\n")
'''for i in quux:
    for item in i:
        if item == "description":
            print(item, "\n")#print(quux)

for titulo in range(len(quux)):
    print("{}".format(foobar.item))'''


