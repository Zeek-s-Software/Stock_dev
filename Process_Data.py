import pandas as pd
import csv
import subprocess

def clear():
    subprocess.call("cls", shell=True)

clear()



data = pd.read_csv("DSE.csv")


print(data['Date'])