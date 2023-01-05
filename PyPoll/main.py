# creating the file
import os

# reading the csv file
import csv

# set path for file
filepath = os.path.join('Resources', 'election_data.csv')

# creating list
candidates = []
all_candidates = []
percent_list = []
data = {}
total = 0



# opening the csv
with open(filepath) as csvfile:

    csv_reader = csv.reader(csvfile)
   

   # loopig through 
    for row in csv_reader:
        total +=1
        all_candidates.append(row[2])
        if row[2] in candidates:
            continue
        else:
            candidates.append(row[2])
    total +=1
for i in range(1,len(candidates)):
    count = 0
    for j in range(len(all_candidates)):
        if candidates[i] == all_candidates[j]:
            count +=1
    data[candidates[i]] = count
candidates.remove(candidates[0])

analysis =open("analysis.txt","w")

print("Election Results")
analysis.write("Election Results\n")
print("-----------------------\n")
analysis.write("-----------------------\n")
print("Total Votes: %d"%total)
analysis.write("Total Votes: %d"%total+"\n")
print("-------------------------\n")
analysis.write("-------------------------\n")
for i in candidates:
    percentage = (data[i]/total)*100
    percentage = round(percentage,2)
    percent_list.append(percentage)
    print(i,percentage,"%","(",data[i],")")
    analysis.write("%s : %f(%d)"%(i,percentage,data[i])+"\n")
print("---------------------------\n")
analysis.write("---------------------------\n")
print("Winner:", candidates[percent_list.index(max(percent_list))])
analysis.write("Winner:"+ candidates[percent_list.index(max(percent_list))]+"\n")
print("\t---------------------\n")
analysis.write("\t---------------------\n")

# printing as a text file
analysis.close()