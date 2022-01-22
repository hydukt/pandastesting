from socket import AI_ADDRCONFIG
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#print(df) 

#print(df.columns)

#print(df[['Name','Type 1','HP']])

#iloc is integer location within the dataset. in this case prints first 5 rows.
#print(df.iloc[0:4])

#print(df.iloc[2,1])

#for index, row in df.iterrows():
    #print(index, row['Name'])

#print(df.iterrows)

#print(df.loc[df['Type 1'] == "Fire"])

#print(df.loc[df['Type 1'] == "Grass"])

#print(df.describe())

#print sorting by name
#print(df.sort_values('Name'))

#print sorting by name, descending order
#print(df.sort_values('Name', ascending=False))


#Print, sorting by two values setting ascending for each
#print(df.sort_values(['Type 1','HP'], ascending=[1,0]))

#creates a new field within the data frame - will display total of all other stats for each row
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

#print(df.head(5))

#drops column
#df = df.drop(columns=['Total'])

#print(df.head(5))

#another way of adding columns. uses integer location - first argument is just ":" to indicate all rows, second argument is columsn to be summed
#.sum tells to add for the selected, axis = 1 adds horizontally, 0 would add vertically
#end parameter is always exclusive, so ending at 10 includes 9 but not 10

#df['Total'] = df.iloc[:, 4:10].sum(axis=1)


#cols gets a list of all column values
#cols = list(df.columns.values)

#reorders columns so that total is closer to left
#df = df[cols[0:4] + [cols[-1]] + cols[4:12]]


#print(df.head(5))


#everything prior is strictly changing how data is displayed to us, not changing structure of data itself.
#be careful when using hardcoded numbers for reference because if file column order changes code isn't good anymore

#takes the updated view of the data frame and saves it to new csv. index = false ensures the indexing isn't a column in output
#df.to_csv('modified.csv', index=False)

#outputs to excel
#df.to_excel('modified.xlsx', index =False)

#outputs to txt, separator set to tab
#df.to_csv('modified.txt', index=False, sep='\t')


#filters for grass and poison. within pandas just use & not and. | substitutes for or
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])








