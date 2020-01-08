#Importing the library
from collections import deque

#Creating a Queue
print ("DEQUE creates a FIFO queue")
myQueue = deque([11,22,33,44,55,66,77,88,99])
print("queue starting values:", myQueue)

# remove 44 from queue
myQueue.remove(44)        # search queue and remove value
print("queue removed     #44:", myQueue)

# rotate queue right 1
myQueue.rotate(1)        # search queue and remove value
print("queue rotate right(1):", myQueue)

# rotate queue right 3
myQueue.rotate(3)        # search queue and remove value
print("queue rotate right(3):", myQueue)

# clear queue 
myQueue.clear()        # search queue and remove value
print("queue clear all data :", myQueue)


