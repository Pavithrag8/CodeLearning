
def create_pair(first, second):
    pair = (first, second)
    return pair

def car(pair):
    return pair[0]

def cdr(pair):
    return pair[1]
pair = create_pair("Coffee", "Tea")
first = car(pair)
second = cdr(pair)
print "First of pair is: {}, Second of pair is: {}".format(first, second)
