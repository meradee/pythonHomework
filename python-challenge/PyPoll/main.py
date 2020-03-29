import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
  pyPoll = csv.reader(csvfile, delimiter=',')

  csvHeader = next(pyPoll)

  votesList =[]
  candidateList =[]

  for row in pyPoll:
    votesList.append(row[2])
    if row[2] not in candidateList:
      candidateList.append(row[2])

# Total Votes
  with open('file.txt', 'w') as outfile:
    totalVotes = len(votesList)
    print("Election Results")
    print("Total Votes: " + str(totalVotes))

    outfile.write("Election Results")
    outfile.write("Total Votes: " + str(totalVotes))