# datapoints = [12,12.5, 13, 13.5, 14]
#
# class_probs = [0.33, 0.39, 0.28]
#
# for dp in datapoints:
#     for i, cp in zip(range(1, 4), class_probs):
#         print(dp, ' - ', i, ' - ',  dp*cp)
#     print('*'*50)

l1 = [1, 2, 3, 4, [8, 9]]
# l2 = l1.copy() #[1, 2, 3, 4, [0, 9]] [-1, 2, 3, 4, [0, 9]]
# l2 = l1[:] #[1, 2, 3, 4, [0, 9]] [-1, 2, 3, 4, [0, 9]]
# l2 = list(l1) #[1, 2, 3, 4, [0, 9]] [-1, 2, 3, 4, [0, 9]]
# import copy
# l2 = copy.copy(l1) #[1, 2, 3, 4, [0, 9]] [-1, 2, 3, 4, [0, 9]]

import copy

l2 = copy.deepcopy(l1)  # [1, 2, 3, 4, [8, 9]] [-1, 2, 3, 4, [0, 9]] Deep

l2[0] = -1
l2[-1][0] = 0

print(l1, l2)


def is_palindromic(s):
    # Note that s[~i] for i in [0, len(s) - 1] is s[-(i + 1)].
    print(list(~i for i in range(10)))
    return all(s[i] == s[~i] for i in range(len(s) // 2))


print(is_palindromic('abcdeeeeeeeedcba'))
print('{0:08b}'.format(2))

print('{0:08b}'.format(~2))
print(~2)
