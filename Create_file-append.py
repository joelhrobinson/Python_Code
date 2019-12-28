import os           ## import os operating sytem library
os.getcwd()
os.chdir ("L:/SOFTWARE/PYTHON/TEMP")
os.getcwd()
## create the file manually
filename = 'createdtoday.txt'
with open(filename) as f_obj:
 contents = f_obj.read()
print(contents)
#################################
#APPEND FILE
with open(filename, 'a') as f:
 f.write("I also love working with data.\n")
 f.write("I love making apps as well.\n")
 f.write("Hello world %d\r\n" )
f.close()