"""
Difficulty: Easy
Category: Arrays


There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic 
problems as fast as possible. Teams compete in a round robin, where each team faces off against all other teams. Only two teams
compete against each other at a time, and for each competition, one team is designated a home team, while the other team is
the away team. In each competition theres's always one winner and one loser; there are no ties. A team receives 3 points if it
wins and 0 points if it loses. The winner of the tounrmanet is the team that receives the most amount of points.

Given an array of pairs representing the teams that have competed against each other and an array containing the results of each
competition, write a function that returns the winner of the tournament. The input arrays are named competitions and results, 
respectively. The copmetitions array has elements in the form of [homeTeam, awayTeam], where aa 1 in the results array means that
the home team in the corresponding competition won and a 0 means that the away team won.

It's guaranteed that exactly one team will win the tounrmanet and that each team will compete against all other teams exactly
once. It's also guaranteed that the tournament will always have at least two teams.

"""

"""
tests

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]

results = [0, 0, 1]
"""

def tournament(competitions, results):
    best_team = ""
    scores = {}

    for idx, game in enumerate(competitions):
        scores.setdefault(game[0],0)
        scores.setdefault(game[1],0)
        
        if results[idx] == 1:
            scores[game[0]] += 3
        if results[idx] == 0:
            scores[game[1]] += 3
        
    best_team = max(scores, key=scores.get)

    return best_team


#print(tournament(competitions, results))