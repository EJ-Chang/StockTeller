# -*- coding: utf-8 -*-

"""
Created on Mon Oct 4 2021

Written by EJ_Chang
"""

# Practice 01

import requests
import json
import numpy as np
import pandas as pd

# TSM website(data from yahoo)
site = "https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"

# request data from the site 
response = requests.get(site)

print(type(response))
# this line returns: 
# <class 'requests.models.Response'>
# EJ: what does that mean?!


# --- below are demo codes
# # Transform data into dataframe
# data = json.loads(response.text)
# df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))

# print(df.head())