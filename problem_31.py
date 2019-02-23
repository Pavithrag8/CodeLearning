'''Given two strings, compute the edit distance between them.'''

string1 = "kitten"
string2 = "sitting"

large_string = string1 if len(string1) >= len(string2) else string2
substitute_count = 0
char_count = 0

for char1, char2 in zip(string1, string2):
    char_count += 1
    if char1 != char2:
        substitute_count += 1
if char_count != len(large_string):
    substitute_count += len(large_string) - char_count

print "Distance between two strings is: {}".format(substitute_count)

