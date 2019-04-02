# Birthday Problem

number_of_days_in_year = 365

probability_of_not_having_any_pair = 1

for person in range(365):
    probability_of_not_having_any_pair *= (365 - person) / 365

    print(person + 1, 1 - probability_of_not_having_any_pair)
