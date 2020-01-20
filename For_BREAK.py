############# tag_name ###############################

for x in range(1, 11):
    for y in range(1, 11):
        print('%d * %d = %d' % (x, y, x*y))
        if x*y > 70:
            print ("BREAK")
            break

for x in range(0, 10):
    print("We're on time %d" % (x))
    if x == 5:
        print ("BREAK")
        break
print ("Joel: Done")
