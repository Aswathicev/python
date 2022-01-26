import csv
with open("Department.csv","w",newline='') as file:
 write=csv.writer(file)
 write.writerow(["Sl No","Department","class"])
 write.writerow(["1","MCA","S1"])
 write.writerow(["2","Computer Science","S2"])
with open("Department.csv") as csvfile:
 data=csv.DictReader(csvfile)
 for r in data:
   print(r['Sl No'],r['Department'])