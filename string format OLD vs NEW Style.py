# simplest style
name = 'Bob'
print ('Hello, %s', % name)
# # old style using .format
print('This is a string {}'.format('INSERTED'))        # print old style format 
print('This is a string {}' .format ('INSERTED'))      # spaces don't matter

# old style using .format with string variables
print('0 El  {fox} was here' .format (fox='Zorro') )
print('1 The {} {} {}' .format('quick',  'brown', 'fox'))       # default order 
print('2 The {2} {0} {1}' .format('quick',  'brown', 'fox'))     # specify order
print('3 The {q} {b} {f}' .format(q='quick', b= 'brown', f='fox'))    # use names

# old style using .format with variables
result= 1 + 2/3
print ( 'old style floating point={r:9.3f}' .format (r=result))    # use "f" 
########################################
# NEW style using print f with variables 
print (result)
print ({result})    # puts brackets in output
print ((result))    # does NOT put parenthesis in output
print (f'{result}')
print (f'new style print (f Unformatted result here {result}')
print (f'new style print (f Formatted   result here   {result:6.3}')

# NEW style using print f with variables 
s ,t = 'yarn' ,'thread'
print ('print  two strings %s and  %s' %(s,t))
print (f'print(f two strings here %s and %s  {s,t}')

# OLD style using .format
print ('{0:8} | {1:9}' .format('Fruit', 'Quantity'))
print ('{0:8} | {1:8}' .format('Apple', 33))
print ('{0:8} | {1:8}' .format('Pears', 22))