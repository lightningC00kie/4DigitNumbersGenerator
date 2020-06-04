import os
threeZero = '000'
twoZero = '00'
oneZero = '0'
f = open('4DigitNumbers.txt', 'a')
for i in range(0,1000):
    numZero = 4 - len(str(i))
    if numZero == 3:
        newStr = threeZero + str(i)
    elif numZero == 2:
        newStr = twoZero + str(i)
    elif numZero == 1:
        newStr = oneZero + str(i)
    print(newStr)
    f.write('\n%s' % (newStr))
for i in range(1000, 10000):
    f.write('\n%s' % (str(i)))
f.close()