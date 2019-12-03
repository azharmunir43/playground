# # A word that reads the same from left to right and right to left is a palindrome.
# # For example, "I", "noon" and "racecar" are palindromes.
# # In this question, we consider palindromic integers such as 101 and 66.
# # * Note that the first digit of an integer cannot be 0.
#
# # How many positive 5-digit integer palindromes
# # How many positive 5-digit even palindromes
# # How many 5 Digit Integer Palindromes - Containing 7 Or 8
# #
#
from itertools import product, combinations, permutations

x = list(range(1, 7))
# x = ['A', 'A', 'A', 'E', 'E', 'E', 'E', 'E']
# x = list(range(0, 10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = list(permutations(x, 2))
print(len(perms))
# all_perms = set(list(product(x, repeat=8)))
# print(len(set(all_perms)))
c = 0
for i in perms:
    # if i[0] == i[-1] == 'E':
    # print(i)
    # c+=1
    print(i, abs(i[0] - i[1]))
print(c)
#
# all_without_zero_on_front = list(filter(lambda x: x[0] != 0, all_perms))  # 0 on front leaves us with 4 digits.
#
# palindromes = []
# all_int_combs = []
#
#
# def is_palindrome(perm):
#     reverse = int(str(perm)[::-1])
#     if reverse == perm:
#         return True
#     else:
#         False
#
#
# for perm in list(all_without_zero_on_front):
#     perm_number = int(''.join(map(str, perm)))  # tuple to number
#     all_int_combs.append(perm_number)
#     if is_palindrome(perm_number):
#         palindromes.append(perm_number)
# #
#
# even_palindromes = list(filter(lambda x: x % 2 == 0, palindromes))
#
# contain_7 = list(filter(lambda x: '7' in str(x), palindromes))
# contain_8 = list(filter(lambda x: '8' in str(x), palindromes))
# contain_7_and_8 = list(filter(lambda x: '8' in str(x) and '7' in str(x), palindromes))
# with_consecutive_4 = list(filter(
#     lambda x: (str(x)[0] == str(x)[1] == str(x)[2] == str(x)[3]) or (str(x)[4] == str(x)[3] == str(x)[2] == str(x)[1]),
#     all_int_combs))
# print(with_consecutive_4)
#
# print('5 Digit Integer Palindromes ' + str(len(palindromes)))
# print('5 Digit Integer Palindromes - Even ' + str(len(even_palindromes)))
#
# # Using Principle of Inclusion Exclusion
# print('5 Digit Integer Palindromes - Containing 7 Or 8 ' + str(len(contain_7) + len(contain_8) - len(contain_7_and_8)))
