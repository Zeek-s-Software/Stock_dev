#import tensorflow as tf
import pandas as pd
import subprocess
import datetime as dt
import numpy
import time
import statistics

#Get the low for 30 days
#add buying

start_num = input('Starting number: ')
start_num = int(start_num)
start_num_30 = (start_num - 30)

money = (100)

Date, Open, High, Low = ('', '', '', '',)

def clear():
    subprocess.call("cls", shell=True)

def Get_Numbers(x):
    data = pd.read_csv('DSE-1.csv')
    df = pd.DataFrame(data)
    Date = data['Date'].iloc[x]
    Open = data['Open'].iloc[x]
    High = data['High'].iloc[x]
    Low = data['Low'].iloc[x]
    return Date, Open, High, Low

clear()

def get_month_numbers():
    x = (start_num)
    month_low = []
    month_high = []
    #Numbers for 30days
    while x < (start_num + 30):
        x = x + 1
        Date, Open, High, Low = Get_Numbers(x)  
        month_low.append(Low)
        month_high.append(High)

    month_low = statistics.mean(month_low)
    month_low = (round(month_low, 2))

    month_high = statistics.mean(month_high)
    month_high = (round(month_high, 2))

    print ('High:',month_high)
    print ('Low:',month_low)
    return month_high, month_low

def buy(money):
    month_high, month_low = get_month_numbers()
    xyz = (start_num + 31)
    while True:
        Date, Open, High, Low = Get_Numbers(xyz)
        if Low < (month_low):
            print ('Buying:', xyz)
            money = (money - Low)
            print ('Bought:', 'DSE')
            print ('Money:', money)
            break
        else:
            xyz = (xyz + 1)

#def sell(money):
#    print()

buy(money)