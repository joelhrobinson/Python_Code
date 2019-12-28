# Udemy strings.py
pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
mypet = input("Enter your type pet: ")
pets.append(mypet)
print('list with all pets', pets)
while 'cat' in pets:
    pets.remove('cat')
print('list without cats',pets)