import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('IMVA.xls', sheet_name='IMVA')
dataSplit = data['Periods'].str.split(' ', n=1, expand=True)
data = data.assign(Year=(dataSplit[0]))
Asia2 = data[((data['Year'] >= str(1988)) & (data['Year'] <= str(1997)))]
countryFilter = Asia2.filter(items=['Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Thailand', 'Vietnam', 'China', 'Hong Kong SAR', 'Taiwan', 'Japan', 'South Korea', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Iran', 'Kuwait', 'Israel', 'Saudi Arabia', 'United Arab Emirates'])

df = pd.DataFrame(countryFilter)
df = df.assign(Year=(dataSplit[0]))
df.index = df['Year']
del df['Year']
df = df.replace(',', '', regex=True)
df = df.replace('na', '0', regex=True)
df = df.astype(int)
totalDF = df.sum(axis=0)
totalDF = totalDF.sort_values(ascending=False)
print('\n------Highest Amount of Travellers-------\n' + str(totalDF))
totalDFs = totalDF.head(3).sum()
print('\n---Top 3 countries---\n' + str(totalDF.head(3)))
print('\n---Bottom 3 countries---\n' + str(totalDF.tail(3)))
meanDF = totalDFs / 3
print('The total no. of visitors for the top 3 countries is ' + str(totalDFs))
print('The mean value for the top 3 countries is ' + str(meanDF.round(2)))
df2 = pd.DataFrame(totalDF)
df2 = df2.assign(Country=(df2.index))
df2 = df2.assign(Total=(df2[0]))
del df2[0]
ps = df2['Total'].sort_values(ascending=False) / 1000
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=15)
plt.ylabel('Total amount of Travellers (in thousands)', fontsize=10, rotation=90)
plt.xticks(index, (ps.index), fontsize=10, rotation=90)
plt.title('All countries from 1988-1987')
plt.bar(ps.index, ps.values)
plt.tight_layout()
plt.savefig('BarchartAll.png')
plt.show()
df2 = df2.head(3)
ps = df2['Total'].sort_values(ascending=False) / 1000
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=15)
plt.ylabel('Total amount of Travellers (in thousands)', fontsize=10, rotation=90)
plt.xticks(index, (ps.index), fontsize=10, rotation=90)
plt.title('All countries from 1988-1987')
plt.bar(ps.index, ps.values)
plt.tight_layout()
plt.savefig('BarchartAll.png')
plt.show()
