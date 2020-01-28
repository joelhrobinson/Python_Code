import sys
s = sys.version_info[0]
t = sys.version_info
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")
print ("Python version =", s, t)
