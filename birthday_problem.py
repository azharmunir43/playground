# Birthday Problem

# How many people musy be in the room such that the probability of having a pair with same birthday exceeds 50pc?

# Assumptions
#   1. 365 days in year, no leap year case.
#   2. Each person's birth is independent, no twins etc.
#   3. Each day is equally likely.


number_of_days_in_year = 365

probability_of_not_having_any_pair = 1

for person in range(365):
    probability_of_not_having_any_pair *= (365 - person) / 365

    print(person + 1, 1 - probability_of_not_having_any_pair)
