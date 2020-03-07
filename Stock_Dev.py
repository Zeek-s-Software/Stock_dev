#Created By BlessingGull250 AKA Ezekiel Bailey
#IF you need help just email me at zeek.bailey3831@gmail.com with the subject "StockDev"
from bs4 import BeautifulSoup
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import matplotlib
import numpy
import requests
import math
import time
import datetime
import re

print ("Your Api key Alpha Vantage")
api_key = input()

t = str(datetime.datetime.today())
ft = ("2015-01-01")
print (t)
print (ft)


ts = TimeSeries(api_key, output_format='pandas')
data = ts.get_intraday(symbol='ICLN', interval='1min', outputsize='compact')
print (data)

#Displaying
p = (10)
divp = (5.6)
d = (divp / 4)
pd = (p / 5)
profit = (0)

def display():
    print ("\n########################")
    print ("Dividend percentages")
    print ("Quaterly")
    print (d)
    print ("Yearly")
    print (divp)
    print ("########################")
    print ("Buy Price")
    print (pd)
    print ("########################")
