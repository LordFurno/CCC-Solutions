games=[]
wins=0
for i in range(6):
  games.append(str(input("")))
for a in games:
  if a=="W":
    wins+=1
if wins==5 or wins==6:
  print(1)
elif wins==3 or wins==4:
  print(2)
elif wins==1 or wins==2:
  print(3)
elif wins==0:
  print(-1)