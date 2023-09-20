n=int(input(""))
timePoints=[]
possibleSpeeds=[]
for a in range(n):
    timePoints.append(tuple(map(int,input("").split(" "))))

timePoints.sort(key=lambda x:x[0])
for a in enumerate(timePoints):
    if a[0]!=len(timePoints)-1:
        startTime=timePoints[a[0]][0]
        endTime=timePoints[a[0]+1][0]
        timeDifference=abs(endTime-startTime)

        startDistance=timePoints[a[0]][1]
        endDistance=timePoints[a[0]+1][1]
        DistanceDiff=abs(endDistance-startDistance)

        possibleSpeeds.append(DistanceDiff/timeDifference)
print(max(possibleSpeeds))