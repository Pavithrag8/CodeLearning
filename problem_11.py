'''Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.'''

import re

def get_possible_autocomplete_strings(query_string, set_of_strings):
    pattern = r'''^{}.*'''.format(query_string)
    regex_pattern = re.compile(pattern)

    possible_autocomplete_strings = []
    for each_string in set_of_strings:
        if regex_pattern.match(each_string):
            possible_autocomplete_strings.append(each_string)
    return possible_autocomplete_strings

possible_autocomplete_words = get_possible_autocomplete_strings("auto", ["autocomplete", "autostart", "autumn"]) 
print "possible autocomplete words are",possible_autocomplete_words