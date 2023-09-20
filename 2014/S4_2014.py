n=int(input())
t=int(input())
boards={}
# start=time.time()
count=set([])
inputs=[]
for a in range(n):
    value=list(map(int,input().split(" ")))
    inputs.append(value)
    
    
    
    
for value in inputs:
    tint=value[-1]
    x1,y1=value[0],value[1]
    x2,y2=value[2],value[3]

    startX=value[0]
    startY=value[1]

    for c in range(x2-x1):
        for b in range(y2-y1):
            topLeft=(startX+c,startY+b)
            topRight=(topLeft[0]+1,topLeft[1]+1)
            if (topLeft,topRight) not in boards.keys():
                boards[(topLeft,topRight)]=tint
                if boards[(topLeft,topRight)]>=t:
                    count.add((topLeft,topRight))
            else:
                temp=boards[(topLeft,topRight)]
                boards[(topLeft,topRight)]=temp+tint
                if boards[(topLeft,topRight)]>=t:
                    count.add((topLeft,topRight))
# end=time.time()
# print(end-start)
print(len(count))
# print(count)
# print(boards)