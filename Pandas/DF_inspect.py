import pandas as pd

# dictionary data
psiList = [{'region': 'east', 'date': '16 Jul 2015', 'psi': '250'},
           {'region': 'south', 'date': '21 Jun 2020', 'psi': '401'},
           {'region': 'west', 'date': '25 Sep 2009', 'psi': '340'},
           {'region': 'north', 'date': '3 Jun 2010', 'psi': '190'}]

psiList2 = [{'region': 'northeast', 'date': '30 Jul 2020', 'psi': '300'},
           {'region': 'southwest', 'date': '20 Jun 2021', 'psi': '200'}]

# create Dataframe from dictionary
df1 = pd.DataFrame(psiList)
df2 = pd.DataFrame(psiList2)

# Get first 2 rows from the dataframe
print(df1.head(2))
print("\n")# new line
# Get last 1 row from the dataframe
print(df1.tail(1))
print("\n")# new line
# To sort the PSI values in descending order
print(df1.sort_values('psi', ascending=False))
print("\n")# new line
# To add df1 to df2 (concatenate both dataframe)
print(pd.concat([df1,df2]))


