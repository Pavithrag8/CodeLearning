number_list = [-1,5,6,0,2,3,1,-1,9,4]
number_list = [0,1,2,3,4,5]
number_list = [4,3,2,1,0,3,2]
def get_missed_least_positive_number(number_list):
    for index, num in enumerate(number_list):
        if index not in number_list:
            return index
    return index+1
missed_positive_num = get_missed_least_positive_number(number_list)
print "Positive number is: ",missed_positive_num