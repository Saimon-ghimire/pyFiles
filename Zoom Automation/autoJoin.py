#!/usr/bin/env python3
from datetime import datetime
import webbrowser

routine = {
    'day': ('period1','period2'),
    #....................
}

def findPeriodNo(hr,min): #which class (class number) at which time
 Class=(
 1 if hr==8 
 else 2 if hr==9 
 else 3 if hr==10 and min>30 or hr==11 and min<20 
 else 4 if hr==11 and min>30 or hr==12 and min<20 
 else 5 if hr==12 and min>40 or hr==13 and min<30 
 else 6 if hr==13 and min>40 or hr==14 and min<30 
 else print('dk which class to join')
 )
 return Class-1

idInfo = {
    'key': ('PMI', "password", "link")
}


now = datetime.now()

key=routine[now.strftime('%A').lower()][findPeriodNo(int(now.strftime("%H")),int(now.strftime("%M")))]
url = idInfo[key][2]
webbrowser.open(url)






