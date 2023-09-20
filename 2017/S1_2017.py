n=int(input(""))
team1=list(map(int,input("").split(" ")))
team2=list(map(int,input("").split(" ")))

count1=0
count2=0

k=0
allK=[]
for index in range(n):
    count1+=team1[index]
    count2+=team2[index]

    if count1==count2:
        k=index+1
        
    if index==n-1:
        allK.append(k)
        break
        
    if count1!=count2 and k!=0:
        allK.append(k)
        k=0

if allK!=[]:
    print(max(allK))
else:
    print(0)