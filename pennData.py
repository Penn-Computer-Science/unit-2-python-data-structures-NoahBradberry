import pandas as pd
import random

fNames = ["Dave", "Mack", "Daniel", "Aiden", "Ben", "Joey", "Christina", "Noah", "Matthew", "Markus", "Jordan", "Josh", "Patrick", "Stephanie", "Jill", "Jane", "Emma", "Catherine", "Rachel", "Marge", "Lisa"]
lNames = ["Smith", "Jones", "Johnson", "Lewis", "Brown", "Garcia", "Davis", "Miller", "Savoie", "Anderson", "Rulli", "Bradberry", "Patel", "Robinson", "Jordan"]
years = ["Freshmen", "Sophomore", "Junior", "Senior", "Victory Lap"]
pathways = ["Early College", "Engineering", "Computer Science", "Business", "Marketing", "Early Childhood Education", "Culinary", "Criminal Justice", "Bio Med"]
names = []

for i in range(20000):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")

data = {
    "Name" : names,
    "Age": [random.randint(14, 19) for _ in names],
    "GPA" : [round(random.uniform(0.3, 4.3),2) for _ in names],
    "Credits Completed" : [random.randint(0,60) for _ in names],
    "Year" : [random.choice(years) for _ in names],
    "Pathway" : [random.choice(pathways) for _ in names]
}

pennData = pd.DataFrame(data)
print(pennData)
pennData.to_csv('pennData.csv', index=False)