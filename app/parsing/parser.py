import requests
from bs4 import BeautifulSoup
import json
import os
from pathlib import Path

CURRANT_DIR = Path(__file__).parent

PROJECT_ROOT = CURRANT_DIR.parent.parent
EXPORTS_DIR = PROJECT_ROOT/'exports'
MASTER_JSON_PATH = EXPORTS_DIR/'master.json'

url = "https://www.rbc.ru/"
headers = {'User-Agent': 'Mozilla/5.0'}

def parse_currency_rates():
    try:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text,'html.parser')
        containers = soup.find_all('a',class_='indicators-bar-item')
        data = []

        for idx,item in enumerate(containers,1):
            name = item.find('span',class_='indicators-bar-name').get_text(strip=True)

            rate = item.find('span',class_='indicators-bar-sum').get_text(strip=True)

            diff = item.find('span',class_='indicators-bar-diff').get_text(strip=True)

            data.append({
                "id":idx,
                "name":name,
                "sum":rate,
                "diff":diff
            })
        return data
    except:
        pass

def save_json(data):
    try:
        with open(MASTER_JSON_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except:
        pass

def parse():
    currencies = parse_currency_rates()
    if currencies:
        save_json(currencies)



