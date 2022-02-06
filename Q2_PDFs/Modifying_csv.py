# Modifies the Marathi_URLs.csv file slightly to make it cleaner
import pandas as pd 

df = pd.read_csv('Marathi_URLs.csv')
df = df[df.columns[1]]
df2 = pd.DataFrame({'URLs' : df.values})
df2.to_csv('Marathi_URLs_2.csv',index=False)

x = pd.read_csv('Marathi_URLs_2.csv')
print(x)