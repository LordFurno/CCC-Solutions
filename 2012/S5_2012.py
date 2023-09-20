r,c=tuple(map(int,input("").split(" ")))
k=int(input(""))
dp=[["E"]*c for i in range(c)]
dp[0][0]=1
cats=[]
for a in range(k):
    val=tuple(map(int,input("").split(" ")))
    cats.append((val[0]-1,val[1]-1))
    dp[val[0]-1][val[1]-1]=0
for y in range(len(dp)):
    for x in range(len(dp[0])):
        if (y,x)!=(0,0):
            if y==0 and (y,x) not in cats:
                dp[y][x]=dp[y][x-1]
            elif x==0 and (y,x) not in cats:
                dp[y][x]=dp[y-1][x]

            if dp[y][x]=="E":
                dp[y][x]=dp[y][x-1]+dp[y-1][x]
print(dp[r-1][c-1])
