#########################
# function removes false values from a list
# false, none, zero, and ""
def compact(lst):
    print (lst)
    return list(filter(None, lst))

############################################# 

compact([0, 1, False, 2, True, '', "", 3, 'a', 's', 33]) # [ 1, 2, 3, 'a', 's', 34 ]

mystring = [0, 1, False, 2, True, '', "", 3, 'a', 's', 99]
newstring = compact (mystring)
print (newstring)
print ("Done")