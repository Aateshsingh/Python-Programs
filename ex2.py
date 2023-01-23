'''x = int(input("Enter a hours:"))
y = int(input("Enter a minute:"))
if x<12 and y<60:
    print("Good morning")
else:
    print("Good night")'''

import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour:"))
print(hour)
if hour>=0 and hour<12:
    print("Good morning")
elif hour>=12 and hour<17:
    print("Good afternoon")
elif hour>=17 and hour<0:
    print("Good Night")
