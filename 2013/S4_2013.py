import time
import collections
import sys
def search(graph,key):
    queue=collections.deque([key])
    visited=set([key])
    parent={key:None}
    while len(queue)>0:
        currentNode=queue.popleft()
        if currentNode in graph.keys():
            for a in graph[currentNode]:
                if a not in visited:
                    queue.append(a)
                    visited.add(a)
                    parent[a]=currentNode
    return visited


start=time.time()
n,m=tuple(map(int,input().split(" ")))
tallerThan={}
allValues=[]
for a in range(m):
    value=sys.stdin.readline()
    value=tuple(map(int,value.split(" ")))
    allValues.extend([value[0],value[1]])
    if value[0] in list(tallerThan.keys()):
        temp=tallerThan[value[0]]
        temp.append(value[1])
        tallerThan[value[0]]=temp
    else:
        tallerThan[value[0]]=[value[1]]

guess=tuple(map(int,input().split(" ")))
allValues=list(set(allValues))


# print(search(tallerThan,80))

newDict=tallerThan.copy()

# for value in tallerThan.keys():
#     oldValue=newDict[value]
#     taller=list(search(newDict,value))
#     temp=list(set(oldValue+taller))
#     tallerThan[value]=temp

if guess[0] in newDict.keys():
    oldVal=newDict[guess[0]]
    taller=list(search(newDict,guess[0]))
    temp=list(set(oldVal+taller))
    tallerThan[guess[0]]=temp
if guess[1] in newDict.keys():
    oldVal=newDict[guess[1]]
    taller=list(search(newDict,guess[1]))
    temp=list(set(oldVal+taller))
    tallerThan[guess[1]]=temp

# print(search(tallerThan,3,[2]))#End is just something that is the smallest
if guess[0] in tallerThan.keys():
    if guess[1] in tallerThan[guess[0]]:
        print("yes")
    elif guess[1] in tallerThan.keys():
        if guess[0] in tallerThan[guess[1]]:
            print("no")
        else:
            print("unknown")
    else:
        print("unknown")

else:
    if guess[1] in tallerThan.keys():
        if guess[0] in tallerThan[guess[1]]:
            print("no")
        else:
            print("unknown")
    else:
        print("unknown")
end=time.time()
print(end-start)