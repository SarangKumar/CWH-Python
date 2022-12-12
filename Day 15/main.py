
import time
timestamp = int(time.strftime('%H'))
print(timestamp)

if(0<=timestamp<12):
    print('Good Morning')
elif(12<=timestamp<15):
    print('Good Afternoon')
else:
    print('Good Evening')