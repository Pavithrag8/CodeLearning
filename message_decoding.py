'''Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.'''


import string
alphabets = string.lowercase
alphabets_num_map = {}
number = 1
for alphabet in alphabets:
    alphabets_num_map[number] = alphabet
    number +=1

message = "123423"

possible_char = []
for num in range(0,len(message)):
    possible_char.append(message[num])
    print "poss",possible_char
    print "num {}, len msg:{}".format(num,len(message))
    if num+1 == len(message):
        break
    if int(message[num] + message[num+1]) <= 26:
        possible_char.append(int(message[num] + message[num+1]))
possible_char = set(possible_char)
print "possible char",possible_char
print "possible number of messages is: {}".format(len(possible_char))
