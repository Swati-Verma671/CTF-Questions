import requests
from bs4 import BeautifulSoup 
import csv

URL='https://swati-verma671.github.io/Motivational-Quotes/'
r=requests.get(URL)
soup=BeautifulSoup(r.content,'html5lib')
quotes=[]


tables=soup.findAll('div',attrs={'class':'col-md-4'})

for table in tables:
    element=table.find('div',attrs={'class':'perseverance'})
    if(element):
        quote={}
        quote['quote']=element.text
        quotes.append(quote)
    else:
        continue    

filename='solutions_1.csv'
with open(filename,'w',newline='') as f:
    w=csv.DictWriter(f,['S.No.','quote'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
