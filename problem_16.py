'''You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.'''

order_id_list = []

def record(order_id):
    global order_id_list
    order_id_list = [order_id] + order_id_list

def get_last(last_ith_element):
    global order_id_list
    return order_id_list[last_ith_element-1]

record(234)
record(35)
record(22)
record(123)
record(678)
record(858)

last_ith_log = get_last(4)
print "last_ith_log",last_ith_log