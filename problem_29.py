'''Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated 
successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded 
as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists 
solely of alphabetic characters. You can assume the string to be decoded is valid.'''

string = "AAAABBBCCDAACC"
#string = "ABC"
encoded_string = ""
char_count = 1

for i, char in enumerate(string):
    if i == 0:
        continue
    if char == string[i-1]:
        char_count += 1
    else:
        encoded_string += str(char_count) + string[i]
        char_count = 1

print "encoded string is: {}".format(encoded_string)