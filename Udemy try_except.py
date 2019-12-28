print ('start')

# the the "try" block to handle the exception 
try: 
    my_list = []       
    while True: 
        my_list.append(int(input('enter integer: else=stop '))) 
# if input is not-integer, exit loop and print the list 
except: 
    print('you entered:', my_list) 
print ('graceful ending')