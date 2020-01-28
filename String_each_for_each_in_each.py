def get_vowels(string):
    return [each for each in string if each in 'aeiouy'] 


print (get_vowels('foobar') ) # ['o', 'o', 'a']
print (get_vowels('gym') )# []


def decapitalize(str):
    return str[:1].lower() + str[1:]
  
  
print ( decapitalize('FooBar') )     # 'fooBar'
print (decapitalize('JOEL') )   # 'fooBar'