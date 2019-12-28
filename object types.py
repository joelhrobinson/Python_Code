##########################
# this is a list
mylist = [1, "joel", 2, 'henry', 3, 'Robinson', 4, "Brenda"]
print ('mylist=',mylist)
mydict =  {"mykey":"value", "Name":"Frankie"}
print ('mydictionary=',mydict)
mytuple = tuple(mylist)
print ('mytuple=',mytuple)
print (type(mytuple))
################################
# parse strings
mystring = "Hello"
print (" string indexing starts at zero", mystring[0])            # indexing starts at zero
print (" string (1) and string (-1)    ", mystring[1], mystring[-4])   # prints an e and an e
print ("Hello with line feed here: \n world")        # LINE FEED
print ("Hello with tab here: \t world")        # TAB
