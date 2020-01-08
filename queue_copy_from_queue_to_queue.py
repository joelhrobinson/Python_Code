#Importing the library
from collections import deque

#Creating a Queue
print ("DEQUE creates a FIFO queue")
myQueue = deque([11,22,33,44,55,66,77,88,99])
print("myQueue starting  values:", myQueue)

# create an empty queue
copyQueue = deque()
# print("copyQueue starting values:", copyQueue)


# create a reversed copy
sourcelength = len(myQueue) 
# print("Length of source queue:", sourcelength)

i = 0
while i < sourcelength:
    qq = myQueue.popleft()
    # print ("popped= ", qq)
    copyQueue.append(qq)
    i = i + 1
print ("newQueue ending   values:", copyQueue    )



