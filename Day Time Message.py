import time
time1= time.strftime('%H:%M:%S')
print(time1)
time2= int(time.strftime('%H'))
timeHour=time2
time3= int(time.strftime('%M'))
timeMin=time3
if(timeHour<=10):
  print(timeHour,"Hours",timeMin,"Minutes")
  print("Good Morning, Have a nice day")
elif(timeHour<=13):
  print(timeHour-12,"Hours",timeMin,"Minutes")
  print("Have a good day,It is day time")
elif(timeHour<=17):
  print(timeHour-12,"Hours",timeMin,"Minutes")
  print("Good afternoon,Its afternoon time")
elif(timeHour<=20):
  print(timeHour-12,"Hours",timeMin,"Minutes")
  print("Good Evening, it is evening time")
else:
  print(timeHour-12,"Hours",timeMin,"Minutes")
  (Print("Good Night,Its night time, Go to bed"))
