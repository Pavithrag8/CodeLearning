'''Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, 
then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, 
then it should throw an error or return null.
Each method should run in constant time.'''

stack = []
def push(val):
    stack.append(val)

def pop():
    if stack:
        latest = stack[-1]
        stack.remove(stack[-1])
        return latest  

def find_max():
    if stack:
        return max(stack)

push(23)
push(34)
push(15)
push(99)
latest_elem = pop()
max_elem = find_max()

print "Latest element on stack is: {}, max element on stack is: {}".format(latest_elem, max_elem)
