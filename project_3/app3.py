import time
from datetime import datetime as dateTime

hostPath = "C:\\Windows\\System32\\drivers\\etc"
redirect = "127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com",
   "www.youtube.com", "youtube.come"]

workingHoursStart = 8
workingHoursEnd = 17

while True:
   year = dateTime.now().year
   month = dateTime.now().month
   day = dateTime.now().day

   if (dateTime(year, month, day, workingHoursStart) < dateTime.now()
         < dateTime(year, month, day, workingHoursEnd)):
      print("Working hours...")
   else:
      print("Fun Hours...")
      
   time.sleep(5)   