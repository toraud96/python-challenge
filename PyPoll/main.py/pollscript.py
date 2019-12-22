import csv 

file_to_load = "election_data.csv"
file_to_output = "polldata.txt"

# Variables for the script
totalVotes = 0
options = []
candidateVotes = {}
winner = ""
count = 0

# Read/opening the cvs
with open(file_to_load) as data:
    reader = csv.DictReader(data)
    # Loop to find results
    for row in reader:
        print(". ", end=""),
        # Finding total votes
        totalVotes = totalVotes + 1
        # Finding the candidate names
        name = row["Candidate"]
        # loop to keep finding candidate names
        if name not in options:
            options.append(name)
            candidateVotes[name] = 0
        candidateVotes[name] = candidateVotes[name] + 1
# Print results and export data file
with open(file_to_output, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalVotes}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    # loop to find the winner
    for candidate in candidateVotes:
        votes = candidateVotes.get(candidate)
        votePercentage = float(votes) / float(totalVotes) * 100
        # finding the winning vote count and candidate
        if (votes > count):
            count = votes
            winner = candidate
        # Print voter count and percentage then saving to output file
        voter_output = f"{candidate}: {votePercentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        txt_file.write(voter_output)
    # Print info
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Saving to text file
    txt_file.write(winning_candidate_summary)