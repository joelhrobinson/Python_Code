############# use SET to remove dups  ###############################

from collections import Counter
# define function to count the number of occurrences of each letter 
def anagram(first, second):
    print (Counter(first))  # creates a dictionary of letters
    print (Counter(second))
    return Counter(first) == Counter(second)

#######################################
# test the dictionaries
print ( anagram("abcd3t", "t3abcd")  ) # True
print ("done")
