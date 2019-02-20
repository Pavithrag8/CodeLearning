'''Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible 
anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the 
lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it 
(which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from 
"race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".'''

string = "race"
#string = "google"
string = "Pavithra"
def is_palindrome(string):
    reverse_of_string = string[::-1]
    if string == reverse_of_string:
        return True
    return False

def make_palindrome(string):
    if is_palindrome(string):
        return string
    reverserd_string = string[::-1]
    reversed_chars = ""
    for char in reverserd_string:
        reversed_chars += char 
        if is_palindrome(reversed_chars + string):
            return reversed_chars + string

print "given string is: {} and its palindrome is: {}".format(string, make_palindrome(string))