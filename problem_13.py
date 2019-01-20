'''Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".'''

string = "puppetttt"#"abcbab"
k = 2
possible_longest_substring = []
longest_substring_length = 0

for indx in range(0, len(string)):
    temp_string = ""
    distinct_char = []
    i = indx
    index = indx
    while i < indx+k+1:
        if index >= len(string):
            break
        
        if string[index] not in distinct_char:
            if i == indx+k:
                break
            distinct_char.append(string[index])
            i += 1
        temp_string += string[index]
        index += 1
    
    if longest_substring_length <= len(temp_string):
        longest_substring_length = len(temp_string)
        possible_longest_substring.append(temp_string) 

for string in possible_longest_substring:
    if len(string) == longest_substring_length:
        print string
