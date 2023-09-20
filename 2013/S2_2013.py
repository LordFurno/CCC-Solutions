maxWeight=int(input(""))
n=int(input(""))
trainWeights=[]
for a in range(n):
    trainWeights.append(int(input("")))
numTrains=0
if n>=4:
    current=trainWeights[0:4]
    currentSum=sum(current)
    if currentSum<=maxWeight:
        numTrains+=4
        for b in range(4,len(trainWeights)):
            currentSum-=current[0]
            if currentSum+trainWeights[b]<=maxWeight:
                numTrains+=1
                currentSum+=trainWeights[b]
                current.pop(0)
                current.append(trainWeights[b])
            else:
                break

        
    else:
        currentSum=0
        for a in trainWeights:
            temp=currentSum+a
            if temp<=maxWeight:
                currentSum+=a
                numTrains+=1
            else:
                break
    
else:
    currentSum=0
    for a in trainWeights:
        if a+currentSum<maxWeight:
            currentSum+=a
            numTrains+=1
        else:
            break
print(numTrains)
# print(trainWeights)