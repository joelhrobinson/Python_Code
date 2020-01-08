#Importing the library
from collections import deque

#Creating a Queue
print ("putting numbers on queue 1,5,8,9")
queue = deque([1,5,8,9])

#Enqueuing elements to the Queue
print ("Queue append onto queue 7 + 0")
queue.append(7) #[1,5,8,9,7]
queue.append(0) #[1,5,8,9,7,0]

#Dequeuing elements from the Queue
print ("Queue popleft from queue")
ii = queue.popleft()         #[5,8,9,7,0]
jj = queue.popleft()        #[8,7,9,0]
print (ii, jj)
#Printing the elements of the Queue
print("Remainder of queue:", queue)