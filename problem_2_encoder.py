# Problem 29 [Easy]

# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive
# characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
#
# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists
# solely of alphabetic characters. You can assume the string to be decoded is valid.

#
# import re
# input_string = 'AAAABBBCCDAA'
#
#
# if bool(re.search(r'\d', input_string)):
#     pairs = [input_string[i:i+2] for i in range(0, len(input_string), 2)]
#     print([int(x[0])*x[1] for x in pairs])
# else:
#     encoded = {}
#     x = ''
#     for char in input_string:
#         if char != x :
#             x = char
#             count = 1
#         else:
#             count+=1
#         print(count, char)

# print(encoded)
# for k, v in encoded:
#     print(k, v)
import math

# print((-15*0.02) + (-7.5*0.05) + (-2.5*0.13) + (2.5*0.4) + (8.0*0.3) + (14*0.1), math.sqrt(0.36))

total_competes = 35
prob = 0
for i in range(1, 36):
    combs = math.factorial(total_competes) / (math.factorial(total_competes - i) * math.factorial(i))
    prob += combs * (0.95 ** i) * (0.05 ** (total_competes - i))

    print(i, combs, prob, combs * (0.95 ** i) * (0.05 ** (total_competes - i)))
