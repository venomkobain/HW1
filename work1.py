from bs4 import BeautifulSoup as bs
from datetime import datetime, date, time
import requests


sites = []
td = []
brand = []
tnow = datetime.now()
curr_time = tnow.strftime("%m/%d/%Y %H:%M:%S")

url = 'https://openphish.com/'

page = requests.get(url)
soup = bs(page.text, "html.parser")
td = soup.find('td', class_= 'url_entry')
td

for td in td.find_all('td'):
    #print(td)
    url = ""
    target = ""
    time = ""
    row = []
    for td in td.find_all('td'):
        #print(td.text.strip())       
        row.append(td.text.strip())        
    print(row)
    if row:
        url = row[0]
        target = row[1]        
        time = date + " " + row[2]

        datetime_object = datetime.strptime(time,"%m/%d/%Y %H:%M:%S")
        if ((tnow - datetime_object).total_seconds()/60-180)<16:
            #print(row)
            sites.append(row)

