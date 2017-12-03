import simplejson as json
import pandas as pd
from pandas import DataFrame
import numpy as nm
#set ORACLE_HOME=C:/Program Files/Oracle/instantclient_12_2
#set PATH=%ORACLE_HOME%;%PATH%
import cx_Oracle
#import Django
#import csv as csv#
# def infinityboost (filename): #This was the original function call
    # df = pd.read_csv(filename)
    # df.sort_values(['Sales'], ascending=[False])
    # DataFrame.head(df)
    # return df
#import as .json
#export as .json
filename = "C:/Users/mylan/AnacondaProjects/infinityboost/sales.json"
df1 = pd.read_json(filename, orient = "record")
df2 = df1.sort_values(['sale_total'], ascending=[False])
df2 = df2.to_json("sortedsales.json",orient='records')
# infinityboost("C:/Users/mylan/AnacondaProjects/infinityboost/train.csv")
df = pd.read_json("C:/Users/mylan/AnacondaProjects/app.json")
DataFrame.head(df)
