import time
from datetime import datetime as dateTime

hostTemp = ("C:\\Users\\oscar\\Desktop\\Programming\\Python\\Ultimate Course"
            "\\Workspace\\project_3\\hosts")
hostPath = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com",
   "www.youtube.com", "youtube.com"]

workingHoursStart = [0, 10, 13, 16, 20]
workingHoursEnd = [2, 12, 15, 18, 21]

while True:
   year = dateTime.now().year
   month = dateTime.now().month
   day = dateTime.now().day
   
   if any(dateTime(year, month, day, start)
         < dateTime.now()
         < dateTime(year, month, day, end)
         for start, end in zip(workingHoursStart, workingHoursEnd)):
      with open(hostPath, "r+") as file:
         content = file.read()
         for website in websiteList:
            if not website in content:
               file.write(redirect + " " + website + "\n")
      print("Working hours..")
   else:
      with open(hostPath, "r+") as file:
         content = file.readlines()
         file.seek(0)
         for line in content:
            if not any(website in line for website in websiteList):
               file.write(line)
         file.truncate()
      print("Not Working hours..")

   time.sleep(5)   