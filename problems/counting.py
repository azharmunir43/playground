from itertools import chain, combinations


def powerset(iterable):
    # "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


power_set = list(powerset(list(range(1, 7))))

l = [i for i in power_set if len(i) == 2]
print(len(l))
for i in l:
    if i[1] > i[0]:
        print(i)

#
# print(len(power_set))
# print(power_set)
#
# # A intersection B = empty set
# count = 0
# list_ = []
# for i in power_set:
#     for j in power_set:
#         if list(set(i) & set(j)) == []:
#             count += 1
#             # print(i, j)
# print("A intersection B = empty set - ", count)
#
# # A intersection B = {1}
# count = 0
# list_ = []
# for i in power_set:
#     for j in power_set:
#         if list(set(i) & set(j)) == [1]:
#             count += 1
#             # print(i, j)
# print("A intersection B = {1} - ", count)
#
# # |A intersection B| = 1
# count = 0
# list_ = []
# for i in power_set:
#     for j in power_set:
#         if len(list(set(i) & set(j))) == 1:
#             count += 1
#             # print(i, j)
# print("|A intersection B| = 1 - ", count)
#
# # A Union B = [1, 2, 3, 4, 5]
# count = 0
# list_ = []
# for i in power_set:
#     for j in power_set:
#         if list(set(i) | set(j)) == [1, 2, 3, 4, 5]:
#             count += 1
#             # print(i, j)
# print("A Union B = [1, 2, 3, 4, 5] - ", count)
#
# # |A Union B| = 4
# count = 0
# list_ = []
# for i in power_set:
#     for j in power_set:
#         if len(list(set(i) | set(j))) == 4:
#             count += 1
#             # print(i, j)
# print("|A Union B| = 4 - ", count)
