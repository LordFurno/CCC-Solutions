def calculate(mid,people):
    time=0
    for p,w,d in people:
        if p+d<mid:
            time+=abs(mid-d-p)*w
        elif p-d>mid:
            time+=abs(p-d-mid)*w
    return time

n=int(input(""))
people=[]
curMin=float('inf')
curMax=0
for a in range(n):
    value=tuple(map(int,input("").split(" ")))
    if value[0]>curMax:
        curMax=value[0]
    if value[0]<curMin:
        curMin=value[0]
    people.append(value)


searchBlock=list(range(curMin,curMax+1))
curMin=float('inf')
# print(mid)
# exit()
count=0
while True:
    L=searchBlock[0]
    H=searchBlock[-1]
    M=int((searchBlock[0]+searchBlock[-1])/2)
    midTime=calculate(M,people)
    leftTime=calculate(M-1,people)
    rightTime=calculate(M+1,people)
    if min(midTime,leftTime,rightTime)<curMin:
        curMin=min(midTime,leftTime,rightTime)
    if rightTime<leftTime and rightTime<midTime:
        searchBlock=searchBlock[searchBlock.index(M)+1:]
    elif leftTime<rightTime and leftTime<midTime:
        searchBlock=searchBlock[:searchBlock.index(M)+1]
    else:
        break

print(curMin)