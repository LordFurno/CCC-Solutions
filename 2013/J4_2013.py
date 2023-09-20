limit=int(input(""))
N=int(input(""))
chores=[]
for i in range(N):
  chores.append(int(input("")))
counter=0
while True:
  small=min(chores)
  if small<=limit:
    limit-=small
    chores.pop(chores.index(small))
    counter+=1
  else:
    break
print(counter)