# Suppose you're on a game show, and you're given the choice of three doors:
# Behind one door is a car; behind the others, goats.
# You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
# He then says to you,"Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

import random

number_of_doors = 10

total_experiments = 1000

wins_by_sticking = 0
wins_by_switching = 0

for ix in range(total_experiments):
    prize_hidden_in = random.randint(1, number_of_doors)
    door_chosen_by_contestant = random.randint(1, number_of_doors)

    if door_chosen_by_contestant == prize_hidden_in:
        wins_by_sticking += 1
    else:
        wins_by_switching += 1

print('Probability of Winning By Sticking', wins_by_sticking / total_experiments)
print('Probability of Winning By Switching', wins_by_switching / total_experiments)
