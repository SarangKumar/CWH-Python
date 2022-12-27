import time
hour = int(time.strftime('%H'))

if hour >=0 and hour<12:
    print('Good Morning Sir')
elif hour>=12 and hour<17:
    print('Good Afternoon Sir')
else:
    print('Good Evening Sir')