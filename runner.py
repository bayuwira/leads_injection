import requests
import json
from urllib.parse import urlencode
import pandas as pd
import time
from random import randint

url = "https://forms.zohopublic.com/bennyrisanto/form/KarmaGroupBigList/formperma/rQLVoS4gClW6bWVfTuHPiWHQV5-k8WaTexavS-NCq8c/htmlRecords/submit"

df = pd.read_csv('inject_today.csv')
df = df.sample(frac=1).reset_index(drop=True)
bank_data = df.values.tolist()
for i in range(len(bank_data)):
  data={
    "Name_First": bank_data[i][0], #First Name
    "Name_Last": bank_data[i][1], #Last Name
    "Email": bank_data[i][2], #Email
    "SingleLine": "+"+str(bank_data[i][3]), #Phone
    "Dropdown": bank_data[i][4], #Marital Status
    "SingleLine6": bank_data[i][5], #Year of Birth
    "Dropdown2": bank_data[i][6], #Card Type
    "SingleLine22": bank_data[i][7], #Program Name
    "SingleLine5": bank_data[i][8], #Lead Source Description
    "SingleLine21": bank_data[i][9], #Lead Status
    "MultipleChoice": bank_data[i][10], #Lead Locations
    "SingleLine3": bank_data[i][11], #Lead Brand
    "SingleLine4": bank_data[i][12], #Lead Sub Brand
    "SingleLine15": bank_data[i][13], #Lead Regions
    "SingleLine7": bank_data[i][14], #Lead Source
    "SingleLine16": bank_data[i][15] #Country
  }
  payload = urlencode(data)
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html',
    'Cookie': '383aeadb58=09c5710d399dc09aa2aecb5e82cb2421'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.status_code)
  sleep_time = randint(100,300)
  print(f"Next POST will be add after {sleep_time} seconds")
  time.sleep(sleep_time)