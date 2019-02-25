'''Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced 
(well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.'''

open_close_map = {")": "(", "}": "{", "]": "["}

stack = []
def push(char):
    stack.append(char)

def pop(char):
    if stack:
        if stack[-1] == open_close_map[char]:
            stack.remove(stack[-1])
        
def check_for_valid_expression(string):
    
    for char in string:
        if char in open_close_map.values():
            push(char)
        elif char in open_close_map.keys():
            pop(char)
    if stack:
        return False
    return True

if __name__ == "__main__":
    string = "([])[]({})"
    print "Is the given expression is valid: ", check_for_valid_expression(string)
