#Importing the library
from collections import deque

#Creating a Queue
print ("DEQUE creates a FIFO queue")
myQueue = deque([11,22,33,44,55,66,77,88,99])
print("myQueue starting   values:", myQueue)

# create a copy
yourQueue = deque(myQueue)
print("yourQueue starting values:", yourQueue)


# create a reversed copy
reversedQueue = deque(reversed(myQueue)) 
print("reversedQueue data values:", reversedQueue)