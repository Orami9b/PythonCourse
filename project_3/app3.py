import time
from datetime import datetime as dateTime

hostTemp = "hosts"
hostPath = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com",
   "www.youtube.com", "youtube.com"]

workingHoursStart = 10
workingHoursEnd = 17

while True:
   year = dateTime.now().year
   month = dateTime.now().month
   day = dateTime.now().day

   if (dateTime(year, month, day, workingHoursStart) < dateTime.now()
         < dateTime(year, month, day, workingHoursEnd)):
      with open(hostPath, "r+") as file:
         content = file.read()
         for website in websiteList:
            if not website in content:
               file.write(redirect + " " + website + "\n")
      print("Working hours...")
   else:
      with open(hostPath, "r+") as file:
         content = file.readlines()
         file.seek(0)
         for line in content:
            if not any(website in line for website in websiteList):
               file.write(line)
         file.truncate()
      print("Fun Hours...")

   time.sleep(5)   