import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('IMVA.xls',sheet_name="IMVA")
ds = data['Periods'].str.split(' ',n=1,expand = True)

data = data.assign(Year=ds[0])
data.index = data['Year']
print(data)

Asia2 = data[(data['Year'] >= str(1988)) & (data['Year'] <= str(1997))];
print(Asia2.columns)

dict = {"country":['Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Thailand', 'Vietnam', 'China', 'Hong Kong SAR', 'Taiwan', 'Japan', 'South Korea', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Iran', 'Kuwait', 'Israel', 'Saudi Arabia', 'United Arab Emirates']}

df = pd.DataFrame(dict)
print(df)