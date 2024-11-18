import pandas as pd


# dictionary data
psiList = [{'region': 'east', 'date': '16 Jul 2015', 'psi': '250'},
           {'region': 'south', 'date': '21 Jun 2020', 'psi': '401'},
           {'region': 'west', 'date': '25 Sep 2009', 'psi': '340'},
           {'region': 'north', 'date': '3 Jun 2010', 'psi': '190'}]

# create Dataframe from dictionary
df1 = pd.DataFrame(psiList)

# read from python file directory PSI_1.xlsx
df2 = pd.read_excel('PSI_1.xlsx')

print(df1)
print("\n")# new line
print(df2)

# To print the date from Region 'East'
print(df1['date'][0])

# Change the date for east region from 16 July 2015 to 21 Jul 2017
df1['date'][0]= '21 Jul 2017'
print(df1)

# To save the changes to new excel file name as PS3_3.xlsx (in your python file directory)
df1.to_excel('PSI_3.xlsx')