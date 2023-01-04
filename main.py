# creating the file
import os

# reading the csv file
import csv

# set path for file
filepath = os.path.join('Resources','budget_data.csv')

# creating list to store budget_data
budget_data = []
output_data = ""
total_months = 0
total_amount = 0
average_change = []
change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""


# opening the csv
with open(filepath) as csvfile:

    csv_reader = csv.reader(csvfile)
    colunns = next(csv_reader)
    row1 = next(csv_reader)
    total_months += 1 
    previous_pl = int(row1[1])
    total_amount = int(row1[1])

    # looping through the budget_data
    for row in csv_reader:
        total_months += 1 
        total_amount += int(row[1])
        current_pl = int(row[1]) 
        change = (current_pl - previous_pl)
        average_change.append(change)
        previous_pl = int(row[1])


        if greatest_increase < change:
            greatest_increase = change
            greatest_increase_date = row[0]

        if greatest_decrease > change:
            greatest_decrease = change
            greatest_decrease_date = row[0]

   
   
    print(total_months)
    print(total_amount)
    print(average_change)

    
    average = round((sum(average_change)/len(average_change)),2)
    print(average)
   
    # printing the final analysis
    output_data = (f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_amount}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}")

# passing output data throught printing statment
print(output_data)

# printing the final analysis as a text file
outpath = os.path.join('analysis','budget_analysis.txt')

with open(outpath,"w") as text_file:
    text_file.write(output_data)


           
    f"-------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_amount}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}"

