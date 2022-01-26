import csv
f=open("Department.csv","w")
writer=csv.DictWriter(f,fieldnames=["Department","Class"])
writer.writeheader()
writer.writerow({"Department":"MCA","Class":"s1"})
writer.writerow({"Department":"MCA","Class":"s2"})
f.close()
c=0
f=open("Department.csv")
reader=csv.DictReader(f)
for row in reader:
 if c==0:
  print(f'{" ".join(row)}')
  print(f'{row["Department"]},{row["Class"]}')
f.close()