def find_winner(votes):
    # Dictionary to store the count of each candidate's votes
    vote_count = {}

    # Counting the votes for each candidate
    for candidate in votes:
        vote_count[candidate] = vote_count.get(candidate, 0) + 1

    # Finding the maximum vote count
    max_votes = max(vote_count.values())

    # Finding the candidate(s) with maximum votes
    winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]

    # Selecting the lexicographically smallest candidate
    winner = min(winners)

    return winner

# Number of votes
num_votes = int(input())

# Array to store the votes
votes = [input() for _ in range(num_votes)]

# Finding the winner
winner = find_winner(votes)

# Output the winner
print(winner)
