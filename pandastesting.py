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

#print(df.loc[df['Type 1'] == "Fire"])

#print(df.loc[df['Type 1'] == "Grass"])

#print(df.describe())

#print sorting by name
print(df.sort_values('Name'))

#print sorting by name, descending order
print(df.sort_values('Name', ascending=False))


#Print, sorting by two values setting ascending for each
print(df.sort_values(['Type 1','HP'], ascending=[1,0]))
