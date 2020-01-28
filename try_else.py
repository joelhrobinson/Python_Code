
s='hello world'
x=2
y=3.5
try:
    x*y
except TypeError:
    print("An exception was raised")
else:
    print("Thank God, no exceptions were raised.")
try:
    s*y      # can't multiply a string times a real #
    s*1.34      # can't multiply a string times a real #
except TypeError:
    print("An exception was raised")
else:
    print("Thank God, no exceptions were raised.")

#Thank God, no exceptions were raised.