import requests
from bs4 import BeautifulSoup
import csv

URL='https://swati-verma671.github.io/Notebook/'
r=requests.get(URL)
soup=BeautifulSoup(r.content,'html5lib')
tables=[]

for row in soup.findAll('span'):
    table={}
    table['Paragraph']=row.text
    tables.append(table)


filename='solutions.csv'
with open(filename, 'w', newline='') as f:
    w=csv.DictWriter(f,['S.No.','Paragraph'])
    w.writeheader()
    for table in tables:
        w.writerow(table)
