import copy
in_put = [3,4,5,1]

output = []
for index, num in enumerate(in_put):
    product = 1
    temp_lst = copy.deepcopy(in_put)
    temp_lst.pop(index)
    for elem in temp_lst:
        product *= elem
    output.append(product)

print "input",in_put
print "output",output

    
    
   