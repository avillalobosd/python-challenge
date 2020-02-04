import os
import csv
from operator import itemgetter 


poll_csv = os.path.join("./election_data.csv")
votes=[]
count=0
results=[]

with open(poll_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        count=count+1
        votes.append(row[2])

name=""
count=0
countTotal=0
votes.sort()
winner=""


for x in range(len(votes)):
    if x==0:
        name=votes[0]
        count=1
        countTotal=1
    else:
        if x==len(votes)-1:
            countTotal=countTotal+1
            count=count+1
            res={"name":name,"votes":count}
            results.append(res)
        elif name==votes[x]:
            count=count+1
            countTotal=countTotal+1
        else:
            res={"name":name,"votes":count}
            results.append(res)
            name=votes[x]
            count=1
            countTotal=countTotal+1

resultsSorted= sorted(results, key=itemgetter('votes'),reverse = True) 

file1 = open("pypollExport.txt","w")
print("Election Results")
file1.write("Election Results \n")
print("-------------------------")
file1.write("------------------------- \n")
print("Total Votes: "+str(countTotal))
file1.write("Total Votes: "+str(countTotal)+"\n")
print("------------------------- ")
file1.write("------------------------- \n")

for x in range(len(results)):
    print(resultsSorted[x]["name"]+": "+str(round((resultsSorted[x]["votes"]/float(countTotal)*100),3))+"% ("+str(resultsSorted[x]["votes"])+")")
    file1.write(resultsSorted[x]["name"]+": "+str(round((resultsSorted[x]["votes"]/float(countTotal)*100),3))+"% ("+str(resultsSorted[x]["votes"])+") \n")
    
    if(x==0):
        winner=resultsSorted[x]["name"]
    elif resultsSorted[x]["votes"]>resultsSorted[x-1]["votes"]:
        winner=resultsSorted[x]["name"]

print("-------------------------")
file1.write("------------------------- \n")
print("Winner: "+winner)
file1.write("Winner: "+winner)

file1.close() 
