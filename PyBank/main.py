import os
import csv
#using relative file location
csvpath = os.path.join('PyBank/Resources/budget_data.csv')

outputpath = os.path.join('PyBank/analysis/budget_analysis.txt')

#Definitions
# The total number of months included in the dataset
months = []
# The net total amount of "Profit/Losses" over the entire period
profit_losses = []
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
change_list = []
# The greatest increase in profits (date and amount) over the entire period - calculated below

# The greatest decrease in profits (date and amount) over the entire period - calculated below

#Open csv file and start calculations:
with open(csvpath) as csvfile:

    # CSV reader & comma delimiter
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first
    csv_header = next(csvreader)
    #start with data row 1:
    first_row = next(csvreader)

    months.append(first_row[0])
    profit_losses.append(int(first_row[1]))
    previous_value = int(first_row[1])
    # Read each row of data after the header
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
        current_value = int(row[1])
        change = current_value - previous_value
        change_list.append(change)
        previous_value = int(row[1])

#print(len(months)) to check
#print(sum(profit_losses)) to check
average_change = round(sum(change_list)/len(change_list),2)
#print(max(change_list),min(change_list)) to check

max_index = change_list.index(max(change_list))
min_index = change_list.index(min(change_list))
#print(months[max_index], months[min_index]) to check
output_text = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {len(months)}\n"
f"Total: ${sum(profit_losses)}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {months[max_index+1]} (${max(change_list)})\n"
f"Greatest Decrease in Profits: {months[min_index+1]} (${min(change_list)})"

)

print(output_text)

with open(outputpath, "w") as txtfile:
    txtfile.write(output_text)