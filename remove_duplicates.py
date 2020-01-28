############# use SET to remove dups  ###############################


## create function to TEST if there are duplicates
# def all_unique(lst):
    return len(lst) == len(set(lst))
################################################################
x = [1,1,2,2,3,2,3,4,5,6, 6, 99]
y = [1,2,3,4,5]
print (x, y   )
xx = all_unique(x) # False
yy = all_unique(y) # True
print ("were string values unique?", xx, yy   )

x = set(x)   # get rid of dups
y = set(y)
print (x, y   )
