import os
import csv

# Variables
budget_csv = os.path.join("./budget_data.csv")
count=0
total=0
greatest=0
lowest=0
name=[]
pl=[]
change=[]
sumchange=0
prev=0
averageChange=0.00

with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 

    for row in csvreader:
        count=count+1
        total=total+int(row[1])
        name.append(row[0])
        pl.append(int(row[1]))
        # print(row[1])

for x in range(len(pl)):
    if x==0:
       change.append(0)
    else:
        change.append(int(pl[x])-int(pl[x-1]))

for x in range(len(change)):
    sumchange=sumchange+int(change[x])
    if(int(change[x])>greatest):
        # print(change[x])
        greatest=int(change[x])
        nameG=name[x]
        
    if(int(change[x])<lowest):
        # print(change[x])
        lowest=int(change[x])
        nameD=name[x]

averageChange=round(sumchange/float((count-1)),2)
      
print("Financial Analysis")
print("----------------------------")
print("Total Months: "+str(count))
print("Total: $"+str(total))
print("Average Change: "+str(averageChange))
print("Greatest Increase in Profits: "+nameG+" ($"+str(greatest)+")")
print("Greateast Decrease in Profits: "+nameD+" ($"+str(lowest)+")")


