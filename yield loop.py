
start = 1
end = 4
step = 2
def my_range(start, end, step):
    while start <= end:
        print (' Do not yield')
        yield start
        start += step

mylist = ['111', '222', '333', '444']
for i in range(len(mylist)):
    print (mylist[i])

mylist = ['a', 'b', 'c', 'd']
for v in mylist:
    print (v)

print (' Done')