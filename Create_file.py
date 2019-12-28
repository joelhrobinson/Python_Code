### Change the working directory so can use local files
import os           ## import os operating sytem library
os.getcwd()
os.chdir ("L:/SOFTWARE/PYTHON/TEMP")
os.getcwd()
############################################################################

f = open("joel-created-by-python.txt","w+")
## f = open("joel02.txt","w+")
## f = open("joel03txt","w+")
for i in range(10):
    f.write("Hello world %d" % (i+1))
f.close()
print ("done")

## with open("TestAnalysisData.csv") as csv_file:
##   file_reader = csv.reader(csv_file)
## print (file_reader)
