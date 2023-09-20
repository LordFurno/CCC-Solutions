n=int(input(""))
rounds=[]
for a in range(n):
    rounds.append(tuple(map(int,str(input("")).split(" "))))
david=100
antonia=100
for a in rounds:
    if a[0]==a[1]:
        continue
    elif a.index(max(a))==0:#If antonia wins
        david-=max(a)
    elif a.index(max(a))==1:
        antonia-=max(a)
print(antonia)
print(david)