name = '12345'
print (name)
print (name[::-1])

def reverse_string(str):
    return str[::-1]

str_data = 'Game of Thrones'
print (str_data)
print('Reverse String using Python slicing =', reverse_string(str_data))

if __name__ == "__main__":
    print('Reverse String using Python slicing =', reverse_string(str_data))