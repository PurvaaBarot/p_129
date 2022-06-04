import csv

dataset1=[]
dataset2=[]

with open("ourput.csv" , "r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)
with open("bright_stars.csv" , "r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)        
headers1=dataset1[0]
planet_data1=dataset1[1:]

headers2=dataset2[0]
planet_data2=dataset2[1:]

headers=headers1+headers2
planet_data=[]

print(len(planet_data1))
for i in planet_data1:
    planet_data.append(i)

for i in planet_data2:
    planet_data.append(i)

with open("merged_dataset.csv" , "a+") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)