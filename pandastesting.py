import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#print(df) 

#print(df.columns)

#print(df[['Name','Type 1','HP']])

#print(df.iloc[0:4])

#print(df.iloc[2,1])

#for index, row in df.iterrows():
    #print(index, row['Name'])

#print(df.iterrows)

print(df.loc[df['Type 1'] == "Fire"])

print(df.loc[df['Type 1'] == "Water"])

