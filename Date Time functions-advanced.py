##########################################
# exercise date time functions
##
import datetime
import time
#########################################################################
# UTC Time   and MST Time
#########################################################################
mydate = datetime.date.today()
print ('mydate =',mydate)
UTC = datetime.datetime.utcnow()
print ('utctime =', UTC)                 # gets the UTC in London
nowtime = datetime.datetime.now()   # good, returns BOISE date and time
print ('MSTtime =',nowtime)

#########################################
# my birthday
Bdate = datetime.date (1953, 2,14)  #calculate how old I am
print ('My age =', mydate - Bdate)               # Joel is about 24,407 days old 
##############################
mynow = time.time()
mytime = datetime.time()            # bad usage returns zeros
print ('mytime =',mytime)              # bad usage returns zeros
print ('mynow =',mynow)                # bad usage returns milliseconds
nowtime = datetime.datetime.now()   # good, returns date and time
print ('nowtime =',nowtime)
print (Bdate.day)
print (Bdate.year)
print (Bdate.month)
print (Bdate.weekday)
