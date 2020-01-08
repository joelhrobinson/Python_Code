#Importing the library
from collections import deque

#Creating a Queue
print ("DEQUE creates a FIFO queue of numbers")
queue = deque([1,5,8,9])

#Enqueuing elements to the Queue
print ("Queue.APPEND added to queue")
queue.append(7) #[1,5,8,9,7]
queue.append(0) #[1,5,8,9,7,0]

#Dequeuing elements from the Queue
print ("Queue.POPLEFT removes from queue")
ii = -1
jj = -1
ii = queue.popleft()         #[5,8,9,7,0]
jj = queue.popleft()        # THERE IS NO POP RIGHT, ONLY POP LEFT

print ("FIFO= ", ii)
print ("FIFO= ", jj)
#Printing the elements of the Queue
print("Remainder of queue:", queue)