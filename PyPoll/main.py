import os
import csv

pypoll_csv = os.path.join('Resources', 'election_data.csv')

candidates = {}

total_votes = 0

winner_vote = 0
winner_name = ''

county_vote = 0
county_name = ''

candidate_vote = 0
candidate_name = ''

with open(pypoll_csv) as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # loop through all of the rows in the csv
    for row in csvreader:

        total_votes = total_votes + 1

        vote_percent = candidate_vote / total_votes

        candidate_name = row[2]

        if candidate_name in candidates:
            candidates[candidate_name] = candidates[candidate_name] + 1
        
        else:
            candidates[candidate_name] = 1

#Export results to csv file

with open('analysis\election_results.csv' , 'w') as csvfile:

    output = 'Election Results\n------------------'

    print(output)

    csvfile.write(output + '\n')
    
    print('Total Votes: ',total_votes)

    csvfile.write('Total Votes: ' + str(total_votes) + '\n------------------' + '\n')

    for key, value in candidates.items():
        
        if value > winner_vote:
            winner_name = key
            winner_vote = value

        pct = value / total_votes * 100

        output = key + ': ' + str(round(pct, 3)) + '% ' + str(value)

        print(output)
        csvfile.write(output + '\n')

    print('\nWinner: ')
    csvfile.write('\nWinner: ')

    output = winner_name + ' ' + str(winner_vote)

    print(output)
    csvfile.write(output)
    
    #The total number of votes cast
    

    #A complete list of candidates who received votes
    #print.list(candidates)

    #The percentage of votes each candidate won
    #print.list(vote_percent)

    #The total number of votes each candidate won
    #print.list(candidate_vote)

    #The winner of the election based on popular vote.
    #print(winner_name)