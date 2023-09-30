from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
table = soup.find_all("table", {"class": "wikitable sortable"})
total_tables = len(table)
scraped_data = []

tr = table[1].find_all("tr")
for td in tr:
    tableRow = td.find_all("td")
    variable = [i.text.rstrip() for i in tableRow ]
    scraped_data.append(variable)
mass = []
name = []
radius = []
distance = []

for i in range(1,len(scraped_data)):
    name.append(scraped_data[i][0])
    mass.append(scraped_data[i][7])
    distance.append(scraped_data[i][5])
    radius.append(scraped_data[i][8])

headers = ['Star_name','Distance','Mass','Radius']  
output = pd.DataFrame(list(zip(name,distance,mass,radius)), columns=['Star_name','Distance','Mass','Radius'] )
output.to_csv("output.csv", index=True, index_label="id")





