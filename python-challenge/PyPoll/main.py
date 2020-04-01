import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
  pyPoll = csv.reader(csvfile, delimiter=',')
  csvHeader = next(pyPoll)

  votesList =[]
  candidateList =[]

#List name for candidates
  for row in pyPoll:
    votesList.append(row[2])
    if row[2] not in candidateList:
      candidateList.append(row[2])

# Total Votes
  with open('file.txt', 'w') as outfile:
    totalVotes = len(votesList)
    print("Election Results")
    print("Total Votes: " + str(totalVotes))

    outfile.write("\nElection Results")
    outfile.write("\nTotal Votes: " + str(totalVotes))

#Candidate name count 
    votesTally = {candidate:votesList.count(candidate) for candidate in candidateList}
#Candidate percent votes and number of votes
    percentVotes = {candidate:((votesCount/totalVotes)*100) for candidate, votesCount in votesTally.items()}

#Print name of candidate, percent of votes, number of votes with for loop
    for candidate, x in percentVotes.items():
        for k,v in votesTally.items():
          if k==candidate:
            print("".join("{}: {:5.2f}% ({})".format(k,x,v)))
            outfile.write("".join("\n{}: {:5.2f}% ({})".format(k,x,v)))

#Print votes in format
    print("".join("Winner:{}".format(candidate) for candidate, votesCount in votesTally.items() if votesList == max (votesTally.values())))

    outfile.write("".join("\nWinner:{}".format(candidate) for candidate, votesCount in votesTally.items() if votesCount == max(votesTally.values())))