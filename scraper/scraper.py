from bs4 import BeautifulSoup
import requests
import os
import warnings
import time
import numpy as np
import pandas as pd
import string
import random
import json
from datetime import datetime

website = 'https://www.coingecko.com/en'
response = requests.get(website)
soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find('table', {'class':'table-scrollable'}).find('tbody').find_all('tr')
names = []
prices = []
for result in results:
    names.append(result.find('a',{'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
    prices.append(result.find('td',{'class':'td-price price text-right'}).get_text().strip())

data = pd.DataFrame(data = zip(names,prices), columns =['Cryptocurrency','Price'])
data.to_csv('./data/data_latest.csv' , index=False)