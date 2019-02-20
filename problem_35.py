'''Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the 
Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B']'''
array = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
R_count = 0
G_count = 0
B_count = 0
for charcter in array:
    if charcter == 'R':
        R_count += 1
    elif charcter == 'G':
        G_count += 1
    else:
        B_count += 1

array = []
for i in range(0, R_count):
    array.append('R')
for i in range(0, G_count):
    array.append('G')
for i in range(0, B_count):
    array.append('B')

print "sorted_list: {}".format(array)
