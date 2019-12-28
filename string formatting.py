# string formatting  using .format() method
print('This is a string {}'.format('INSERTED'))        # print old style format 
print('This is a string {}' .format('INSERTED'))        # spaces don't matter
print('This is a string {}' .format ('INSERTED'))      # spaces don't matter

# format old style 
print('The {} {} {}' .format('quick',  'brown', 'fox'))        # print 'r'
print('The {2} {2} {1}' .format('quick',  'brown', 'fox'))        # print 'r'
print('The {0} {2} {1}' .format('quick',  'brown', 'fox'))        # print 'r'

print('The {q} {b} {f}' .format(q='quick', b= 'brown', f='fox'))        # print 'r'
#####################################
# formatted string literals
result=1 + 2/3
print ('floating point={r:9.3f}' .format (r=result))    # use "f" to prevent going exponential
print ('floating point={r:1.3f}' .format (r=result))
print ('floating point={r:0.3f}' .format (r=result))
print ('floating point={r:9.3e}' .format (r=result))  # exponential
########################################
# format numbers 
print (f'Unformatted result here {result}')
print (f'Formatted result here   {result:6.3}')
# format strings
s ,t = 'yarn' ,'thread'
print ('I will inject string here %s and here %s' %(s,t))
print (f'Format two strings here %s %s  {s,t}')

print ('{0:8} | {1:9}' .format('Fruit', 'Quantity'))
print ('{0:8} | {1:8}' .format('Apple', 33))
print ('{0:8} | {1:8}' .format('Pears', 22))