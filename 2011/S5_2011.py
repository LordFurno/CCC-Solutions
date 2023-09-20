import collections
def possible(lights):
    possible=[]
    for i,a in enumerate(lights):
        if a==0:
            possible.append((i,lights))
    return possible
def update(index,lights):
    temp=lights[:]
    temp[index]=1

    start=None
    counter=0
    for i,a in enumerate(temp):

        if a==1 and start==None:
            counter+=1
            start=i
        elif a==1:
            counter+=1
        elif a==0 and counter>=4:
            temp=temp[:start]+[0]*counter+temp[i:]
            start=None
            counter=0
        elif a==0:
            start=None
            counter=0
    if start!=None and counter>=4:
        temp=temp[:start]+[0]*counter

    return temp


def shortest(n,start):

    queue=collections.deque([start])
    visited=set((start[0],tuple(start[1])))
    parent={(start[0],tuple(start[1])):None}
    while len(queue)>0:
        current=queue.popleft()
        newLights=update(current[0],current[1])
        if newLights==[0]*n:

            path=[(current[0],tuple(current[1]))]
            while parent[(current[0],tuple(current[1]))]!=None:
                current=parent[(current[0],tuple(current[1]))]
                path.append((current[0],tuple(current[1])))

            return path
    

        possibleMoves=possible(newLights)

        for a in possibleMoves:
            if (a[0],tuple(a[1])) not in visited and (a[0],tuple(a[1]))!=(start[0],tuple(start[1])):
                queue.append(a)
                visited.add((a[0],tuple(a[1])))

                parent[(a[0],tuple(a[1]))]=(current[0],tuple(current[1]))

    return curMin
        # if cu
# 1
# 1
# 0
# 1
# 1
# print(update(1,[1,0,0,0,0,1]))
n=int(input(""))
lights=[]
for a in range(n):
    lights.append(int(input("")))
curMin=float('inf')
possibleMoves=possible(lights)
print(len(possibleMoves))
test=1
for start in possibleMoves:
    print(f"HERE: {test}")
    path=shortest(n,start)
    if len(path)<curMin:

        curMin=len(path)
    test+=1

# print(update(1,[1,0,0,0,0,1]))
print(curMin)
# print(len(shortest(n,start)))