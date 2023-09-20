start_time=list(map(int,input("").split(":")))
minute_time=start_time[0]*60+start_time[1]#In minutes
check_minutes=minute_time
result=0
for i in range(1,121):
  if (minute_time >=420 and minute_time<600) or (minute_time>=900 and minute_time<1140):

    start_time[1]+=2
  else:
    start_time[1]+=1
  minute_time=start_time[0]*60+start_time[1]


if start_time[1]>60:#If minutes greater than 60
  start_time[0]+=start_time[1]//60
  start_time[1]=start_time[1]%60

if start_time[0]>=24:
  multiple=start_time[0]//24
  start_time[0]-=24*multiple

printing=""
if start_time[0]<10:
  printing+="0"+str(start_time[0])+":"
  if start_time[1]<10:
    printing+="0"+str(start_time[1])
  else:
    printing+=str(start_time[1])
else:
  printing+=str(start_time[0])+":"
  if start_time[1]<10:
    printing+="0"+str(start_time[1])
  else:
    printing+=str(start_time[1])
  
print(printing)