n,t=tuple(map(int,input("").split(" ")))
start=list(map(int,list(input(""))))
for a in range(t):
    temp=start[:]
    for a in range(len(start)):
        if a!=len(start)-1:
            nextCell=start[a+1]
            prev=start[a-1]
            if prev^nextCell==0:
                temp[a]=0
            else:
               temp[a]=1
        else:
            nextCell=start[0]
            prev=start[a-1]
            if prev^nextCell==0:
                temp[a]=0
            else:
               temp[a]=1
    start=temp
print(" ".join(map(str,start)))