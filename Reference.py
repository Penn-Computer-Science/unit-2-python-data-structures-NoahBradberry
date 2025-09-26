import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

#Load our Data Frame
df = pd.read_csv("pennData.csv")
pennData = pd.DataFrame(df)
print("-_"*20)
print("Head of the DataFrame") #First 5 lines
print(pennData.head())

print("-_"*20)
print("Tail of the DataFrame") #Final 5 lines
print(pennData.tail())

print("-_"*20)
print("Summary of the DataFrame") #Name of columns, Count of objects, datatype
print(pennData.info())

print("-_"*20)
print("Statistical Analysis") #Count, Mean, Std, Min, 25%, 50%, 75%, max
print(round(pennData.describe())) #Rounds to one decimal (Default is 6)

print("-_"*20)
print("Counts of Students in Pathways") #Prints each Pathway and how many keys that have that pathway
print(pennData['Pathway'].value_counts())

print("-_"*20)
print("Average GPA Per Year") #Prints all Years (In alphabetical) and the average GPA across all students in that year
print(pennData.groupby('Year')['GPA'].mean())

print("-_"*20)
print("Top three students by GPA") #Prints all Data for the Students with the top 3 GPA
print(pennData.sort_values(by='GPA', ascending=False).head(3))

print("-_"*20)
print("Students with GPA > 3.5") #Prints all Data for the students with a higher GPA then 3.5
print(pennData[pennData['GPA']>3.5])

print("-_"*20)
print("First Student Data") #Prints all the data for the first student in multiple lines instead of one.
print(pennData.iloc[0])