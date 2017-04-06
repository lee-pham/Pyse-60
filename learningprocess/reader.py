import time
f = open('/Users/leepham/PycharmProjects/Pyse-60/hallcall.txt', 'r')
for line in f:
    print(line[0:-1])
    time.sleep(.01)
f.close()
