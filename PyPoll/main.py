import os
import csv

csvpath = os.path.join ('PyPoll\Resources\election_data.csv')
outputpath = os.path.join ('PyPoll/analysis/election_result.txt')


# The total number of votes cast
TotalVotes = 0

# a list of all the votes individually
VoteList = []

# A complete list of candidates who received votes
candidates = []

#access csv file
with open(csvpath) as csvfile:

    # CSV reader - delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
        # Read the header row first 
    csv_header = next(csvreader)
    
   

    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
    
        TotalVotes += 1

        VoteList.append(row[2])


#A list of totals for each candidate
VoteTotals = []
# a list of percentage votes for each candidate
VotePercents = []

for x in candidates:

    VoteTotals.append(VoteList.count(x))
    VotePercents.append(round(VoteList.count(x)/TotalVotes*100,3))


max_votes = VoteTotals.index(max(VoteTotals))
winner = candidates[max_votes]


output_text=(
f"Election Results\n"
f"-------------------------\n"
f"Total Votes: {TotalVotes}\n"
f"-------------------------\n"
f"{candidates[0]}: {VotePercents[0]}% ({VoteTotals[0]})\n"
f"{candidates[1]}: {VotePercents[1]}% ({VoteTotals[1]})\n"
f"{candidates[2]}: {VotePercents[2]}% ({VoteTotals[2]})\n"
f"-------------------------\n"
f"Winner: {winner}\n"
f"-------------------------"
)

print(output_text)

with open(outputpath, "w") as txtfile:
    txtfile.write(output_text)
