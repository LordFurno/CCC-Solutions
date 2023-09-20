m=int(input(""))
commands=[]
results=[]
for i in range(m):
    commands.append(tuple(input("").split(" ")))

for a in enumerate(commands):
    if a[1][0]=="R":
        counter=0
        friend=a[1][1]
        end=("S",friend)
        if end not in commands:
            results.append((friend,-1))
        else:
            for c in range(a[0]+1,len(commands)):
                if commands[c][0]=="W":
                    counter+=int(commands[c][1])-1
                elif commands[c]!=end:
                    counter+=1
                if commands[c]==end:
                    counter+=1
                    break
            results.append((friend,counter))
final=[]
for a in results:
    search=a[0]
    temp=0
    for b in results:
        if b[0]==search:
            if b[1]==-1:
                temp=b[1]
                break
            temp+=b[1]
    final.append((search,temp))
final=list(set(final))
final.sort()
for a in final:
    print(str(a[0])+" "+str(a[1]))