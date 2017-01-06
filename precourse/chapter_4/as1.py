import pandas as pd
import numpy as np

df = pd.read_csv('beds.tsv', delimiter='\t')

def qi():
    return df["Facility.ID"].max()
# print qi()
# print df.head(5)

# print df.columns.values.tolist()
def qone():
    return df.head(1).count(axis = 1)
# print qone()

def qtwo():
    return df["Bed.Census.Date"].min()
# print qtwo()

def qthree():
    return df["Bed.Census.Date"].max()
# print qthree()

def qfour():
    return df.sort("Available.Residential.Beds", ascending = False)["Bed.Census.Date"].head(10)
# print  qfour()

def qfive():
    return df.sort("Available.Residential.Beds", ascending=True).head(10)["Bed.Census.Date"]
print qfive()
