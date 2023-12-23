from bs4 import BeautifulSoup
from requests import get
import pandas as pd 

house_details = list()
price_lakh = list()
other_details = list()

df = pd.read_csv('housing_uncleaned.csv')
count =0

for i in range(1,50):
       url = f'target_url{i}'
       req = get(url)
       soup = BeautifulSoup(req.content,'html.parser')
       url_select = soup.select('div.title-line a')
       for i in url_select:
             house_url = i['href'] 

             house_req = get(house_url)
             house_soup = BeautifulSoup(house_req.content,'html.parser')
             house_select = house_soup.select('h1.type-wrap')[0].text
             house_details.append(house_select)

             price_select = house_soup.select('span.price span')[0].text
             price_lakh.append(price_select)

             tbody_select = house_soup.select('tbody')[0]
             other_details.append(tbody_select.text)
              
             print(count)
             count = count+1

df['house_details'] = house_details
df['price_lakh'] = price_lakh
df['other_details'] = other_details

df.to_csv('housing_uncleaned.csv')