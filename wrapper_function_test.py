#testing a wrapper function which returns 0 if v1 or i1 are 0
#this avoids ZeroDivisionError when sensors aren't plugged in
#using only if/elif/else
v1 = 0
i1 = 4

def calcResistance(v1, i1):
    if v1 == 0:
        return 0
    elif i1 == 0:
        return 0
    else:
        return v1/i1

print ("Channel 1 resistance R: %02f" % calcResistance(v1, i1))
