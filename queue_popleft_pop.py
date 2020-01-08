#Importing the library
from collections import deque

#Creating a Queue
print ("DEQUE creates a FIFO queue")
myQueue = deque([1,5,8,9])

#Enqueuing elements to the Queue
print ("myQueue.append(99) & myQueue.appendleft(66)")
myQueue.append(99)        # put value on DEFAULT side of queue (RIGHT)
myQueue.appendleft(66)    # put value on LEFT side of queue
print("print queue:", myQueue)
#Dequeuing elements from the Queue
print ("myQueue.POPLEFT removes from queue")
ii = myQueue.popleft()        #[5,8,9,7,0]
jj = myQueue.pop()          # POP RIGHT

print ("FIFO= ", ii)
print ("FIFO= ", jj)
#Printing the elements of the Queue
print("print queue:", myQueue)
x = len(myQueue) 
print ("length of queue:", x )
