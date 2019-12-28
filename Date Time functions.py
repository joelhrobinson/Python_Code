##########################################
# exercise date time functions
# nieve date have no time zone information
#
import datetime
# exercise date functions
now = datetime.date (1953, 2,14)          # YYYY MM DD integers only
print ('Date of birth   ', datetime.date (1953, 2,14) )
print ('Current date    ', datetime.date.today() )

now = datetime.date.today() 
print ('current year is ', now.year)            # just print out the year
print ('current weekday ', now.weekday() )
print ('isoweekday      ', now.isoweekday() )

####################################
# time delta of one week
dnow = datetime.date.today()          # YYYY MM DD integers only
print ('date this week ', dnow)
tdelta = datetime.timedelta(days=7)
print ('date next week ', dnow + tdelta)
print ('date last week ', dnow - tdelta)
print ('diff', tdelta)          # diff seven days



#print (date.today() )
#print (datetime.now() )
#print (date.today() )


#print (date.month() )
#print (date.weekday())

#print ('time   =', datetime.time())
#print ('day    =', datetime.day())
#print ('month  =', datetime.month())
#print ('now    =', datetime.now())
#print ('second =', datetime.second())
#print ('today  =', datetime.today())
#print ('DOW    =', datetime.weekday())
#print ('year   =', datetime.year())
#print ('microsecond  =', datetime.microsecond())