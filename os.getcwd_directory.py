import os           ## import os operating sytem library

mypath = 'L:/SOFTWARE/PYTHON'
os.chdir(mypath)
print (os.path.abspath('.')  )  # print absolute working directory
############################################################
os.getcwd() # The method os. getcwd() in Python returns the current working directory of a process
print (os.getcwd())             # print the working directory

###############################################################
# os.name: name of the operating system dependent module imported. 
# The following names have currently been registered: 
# ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’
print (os.name)        
###############################################################
# os.listdir names of all files and directories in current folder
print ( os.listdir('.') )