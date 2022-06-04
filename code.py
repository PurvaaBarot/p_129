import pandas as pd
df=pd.read_csv("dwarf_stars (1).csv")
df=df.dropna()

df['Mass'] = df['Mass'].astype(float)

df["Radius"]=df["Radius"]*0.102763
df["Mass"]=df["Mass"]*0.000954588

df=df.drop(columns='Unnamed: 0')

df.to_csv("ourput.csv")

