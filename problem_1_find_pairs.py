# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Solution: O(n^2)


input_list = [10, 15, 3, 7, 0]


def check_for_pairs(input_list, k):
    for x in input_list:
        for y in input_list:
            if x + y == k:
                return True

    return False


print(check_for_pairs(input_list, 7))
