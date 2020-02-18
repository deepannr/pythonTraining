#5:15:00

import pandas as pd, numpy as np

withNpAndPd = pd.DataFrame({'Row1' : pd.Series(np.arange(-10, 10)),
                            'Row2' : pd.Series(np.arange(0, 40, 2))})

print("withNpAndPd:\n", withNpAndPd)
print("\nPrint only Values:\n", withNpAndPd.values)
print("\nPrint first 5 values:\n", withNpAndPd.head()) #Default is 5
print("\nPrint first 6 values:\n", withNpAndPd.head(6))
print("\nLast 5 values:\n", withNpAndPd.tail())
print("\nLast 6 values:\n", withNpAndPd.tail(6))

evenAndOdd = pd.DataFrame({'Odd' : pd.Series(np.arange(-1, 50, 2)),
                           'Even' : pd.Series(np.arange(0, 52, 2))})

print("\nEven Numbers:", evenAndOdd['Even'])
print("\nOdd Numbers:", evenAndOdd['Odd'])
print("\nSum:\n", evenAndOdd.sum())
print("\nStandard Deviation:\n", evenAndOdd.std())

listColumns = ['col1', 'col2', 'col3', 'col4']

print("\nRandom Values")
randomPds = pd.DataFrame(np.random.rand(5, 4), columns = listColumns)
for key, value in randomPds.iteritems():
    print("Key:", key)
    print("Value:\n", value)
    

npArray = np.arange(51, 71)
npMultiArr = npArray.reshape(4, 5)
colForNpArray = ['C1', 'C2', 'C3', 'C4', 'C5']
pdNpArray = pd.DataFrame(npMultiArr, columns = colForNpArray)

print("\nPrint Panda DataFrame:\n", pdNpArray)

print("\nPrint Column-wise:")
for key, value in pdNpArray.iteritems():
    print("Key:", key)
    print("Values:\n", value)
    
print("\nAnother way Print Column-wise:")
for key, value in pdNpArray.items():
    print("Key:", key)
    print("Values:\n", value)

print("\nPrint Row-wise:")
for key, value in pdNpArray.iterrows():
    print("Key:", key)
    print("Values:\n", value)
    

print("\nTuples for each row:")
for row in pdNpArray.itertuples() :
    print("Row:", row)

print("\nAnother Set of Data Manipulation")
criTeam = ['WI', 'WI', 'Ind', 'Aus', 'Pak', 'SL', 'Aus', 'Aus', 'Aus', 'Ind', 'Aus', 'Eng']
criRank = ['7', '7', '1', '3', '6', '5', '3', '3', '3', '1', '3', '2']
criYear = [1975, 1979, 1983, 1987, 1992, 1996, 2000, 2003, 2007, 2011, 2015, 2020]
criLost = ['Aus', 'Eng', 'WI', 'Eng', 'Eng', 'Aus', 'Pak', 'Ind', 'SL', 'SL', 'NZ', 'NZ']

worldCup = pd.DataFrame({
        'Winner' : criTeam,
        'Loser' : criLost,
        'WinRank' : criRank,
        'Year' : criYear
    })
print("Winners:\n", worldCup.groupby('Winner').groups)
print("Losers:\n", worldCup.groupby('Loser').groups)
print("Winners, Year:\n", worldCup.groupby(['Winner', 'Year']).groups)
print("Losers, Year:\n", worldCup.groupby(['Loser', 'Year']).groups)