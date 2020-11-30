import csv
import pandas as pd 
data = pd.read_csv("C:\\Users\\PC\\Desktop\\data.csv", 'rt')
print(data.head(10))