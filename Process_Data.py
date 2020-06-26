import pandas as pd
import csv
import subprocess
import numpy

def clear():
    subprocess.call("cls", shell=True)

clear()


def Get_Numbers():
    data = pd.read_csv('DSE.csv')
    df = pd.DataFrame(data)
    x = (0)
    Date = data['Date'].iloc[x]
    Open = data['Open'].iloc[x]
    High = data['High'].iloc[x]
    Low = data['Low'].iloc[x]
    return Date, Open, High, Low

Date, Open, High, Low = (Get_Numbers())

