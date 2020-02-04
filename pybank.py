import os
import csv

budget_csv = os.path.join("./budget_data.csv")
count=0
total=0
greatest=0
lowest=0
pl=[]
prev=0

with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 

    for row in csvreader:
        count=count+1
        total=total+int(row[1])
        pl.append(int(row[1]))
        # print(row[1])

for x in range(len(pl)):
    # print(x)
    if x==0:
        prev=int(pl[x])
    else:
        change=int(pl[x]-prev)
        print(change)
        if(change>greatest):
            # print(x)
            greatest=change-prev
            prev=int(pl[x])
        elif (change<lowest):
            # print(x)
            lowest=change
            prev=int(pl[x])

print("Count "+ str(count))
print("Total "+ str(total))
print("Greatest "+ str(greatest))
print("Lowest "+ str(lowest))

