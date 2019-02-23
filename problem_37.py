'''The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.'''
from itertools import chain, combinations

input_set = {1, 2, 3}
power_set = chain.from_iterable(combinations(input_set,n) for n in range(len(input_set)+1))

print "power set for given set is: ",list(power_set)