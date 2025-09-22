import pandas as pd
bnames = ["Noah", "Liam", "Jacob", "William", "Mason", "Ethan", "Michael", "Alexander", "James", "Elijah"]
gnames = ["Emma", "Olivia", "Sophia", "Isabelle", "Ava", "Mia", "Abigail", "Emily", "Charlette", "Madison"]
bfreq = [183330, 173981, 163266, 159945, 157875, 149082, 145171, 142142, 139652, 137093]
gfreq = [195028, 184528, 181132, 170559, 155844, 129088, 118713, 117626, 102470, 98419]
df = pd.DataFrame(
    {
        "Boys Names" : bnames,
        "Boys Frequency" : bfreq,
        "Girls Names" : gnames,
        "Girls Frequency" : gfreq
    }
)
print(df)