# -*- coding: utf-8 -*-
# Author: Morten Helmstedt. E-mail: helmstedt@gmail.com
""" This program extracts historical stock prices from Nordnet (and Morningstar as a fallback) """
 
import requests
from datetime import datetime
from datetime import date
import os
 
# Nordnet user account credentials
user = ''
password = ''
 
# DATE AND STOCK DATA. SHOULD BE EDITED FOR YOUR NEEDS #
 
# Start date (start of historical price period)
startdate = '2013-01-01'
 
# List of shares to look up prices for.
# Format is: Name, Morningstar id, Nordnet stock identifier
# See e.g. https://www.nordnet.dk/markedet/aktiekurser/16256554-novo-nordisk-b
# (identifier is 16256554)
# All shares must have a name (whatever you like). To get prices they must
# either have a Nordnet identifier or a Morningstar id
sharelist = [
["Maj Invest Pension","F0GBR064UH",16099877],
["Novo Nordisk B A/S","0P0000A5BQ",16256554],
["Nordnet Superfonden Danmark","F00000TH8X",""],
]
 
# CREATE VARIABLES FOR LATER USE. #
 
# A variable to store historical prices before saving to csv    
finalresult = ""
finalresult += '"date";"price";"instrument"' + '\n'
 
# A cookie dictionary for storing cookies
cookies = {}
 
# NORDNET LOGIN #
 
# First part of cookie setting prior to login
url = 'https://classic.nordnet.dk/mux/login/start.html?cmpi=start-loggain&state=signin'
request = requests.get(url)
cookies['LOL'] = request.cookies['LOL']
cookies['TUX-COOKIE'] = request.cookies['TUX-COOKIE']
 
# Second part of cookie setting prior to login
url = 'https://classic.nordnet.dk/api/2/login/anonymous'
request = requests.post(url, cookies=cookies)
cookies['NOW'] = request.cookies['NOW']
 
# Actual login that gets us cookies required for later use
url = "https://classic.nordnet.dk/api/2/authentication/basic/login"
request = requests.post(url,cookies=cookies, data = {'username': user, 'password': password})
cookies['NOW'] = request.cookies['NOW']
cookies['xsrf'] = request.cookies['xsrf']
 
# Getting a NEXT cookie
url = "https://classic.nordnet.dk/oauth2/authorize?client_id=NEXT&response_type=code&redirect_uri=https://www.nordnet.dk/oauth2/"
request = requests.get(url, cookies=cookies)
cookies['NEXT'] = request.history[1].cookies['NEXT']
 
# LOOPS TO REQUEST HISTORICAL PRICES AT NORDNET AND MORNINGSTAR #
 
# Nordnet loop to get historical prices
for share in sharelist:
    # Nordnet stock identifier and market number must both exist
    if share[2]:
        url = "https://www.nordnet.dk/api/2/instruments/historical/prices/" + str(share[2])
        payload = {"from": startdate, "fields": "last"}
        data = requests.get(url, params=payload, cookies=cookies)
        jsondecode = data.json()
         
        # Sometimes the final date is returned twice. A list is created to check for duplicates.
        datelist = []
         
        for value in jsondecode[0]['prices']:
            price = str(value['last'])
            price = price.replace(".",",")
            date = datetime.fromtimestamp(value['time'] / 1000)
            date = datetime.strftime(date, '%Y-%m-%d')
            # Only adds a date if it has not been added before
            if date not in datelist:
                datelist.append(date)
                finalresult += '"' + date + '"' + ";" + '"' + price + '"' + ";" + '"' + share[0] + '"' + "\n"
 
# Morningstar loop to get historical prices         
for share in sharelist:
    # Only runs for one specific fund in this instance
    if share[0] == "Nordnet Superfonden Danmark":
        payload = {"id": share[1], "currencyId": "DKK", "idtype": "Morningstar", "frequency": "daily", "startDate": startdate, "outputType": "COMPACTJSON"}
        data = requests.get("http://tools.morningstar.dk/api/rest.svc/timeseries_price/nen6ere626", params=payload)
        jsondecode = data.json()
         
        for lists in jsondecode:
            price = str(lists[1])
            price = price.replace(".",",")
            date = datetime.fromtimestamp(lists[0] / 1000)
            date = datetime.strftime(date, '%Y-%m-%d')
            finalresult += '"' + date + '"' + ";" + '"' + price + '"' + ";" + '"' + share[0] + '"' + "\n"
 
# WRITE CSV OUTPUT TO FILE #            
 
with open("kurser.csv", "w", newline='', encoding='utf8') as fout:
    fout.write(finalresult)