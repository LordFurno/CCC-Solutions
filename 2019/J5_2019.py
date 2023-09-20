import collections

def chunk(value,length):
    chunks=[]
    for a in range(len(value)-length+1):
        chunks.append(value[a:a+length])
    return chunks

def generateMoves(start):
    moves=[]
    for search in rule1,rule2,rule3:
        if search==rule1:
            rule=1
        elif search==rule2:
            rule=2
        else:
            rule=3
        if search[0] in start:
            length=len(search[0])
            chunks=chunk(start,length)
            for index,value in enumerate(chunks):
                temp=start[:]
                if value==search[0]:
                    newVal=temp[:index]+search[1]+temp[index+length:]
                    moves.append((rule,index+1,newVal))
    return moves
# print(chunk("AAA",2))

def findPath(start,goal,steps):
    queue=collections.deque([(0,0,start)])
    visited=set([(0,0,start)])
    parent={(0,0,start):None}
    while(len(queue)>0):
        currentNode=queue.popleft()
        if currentNode[2]==goal:
            curPath=[currentNode]
            while parent[currentNode]!=None:
                currentNode=parent[currentNode]
                curPath.append(currentNode)
            curPath.pop(-1)
            if len(curPath)==steps:
                return curPath
            elif steps<len(curPath):
                return None
        possible=generateMoves(currentNode[2])
        for value in possible:
            if value not in visited and value:
                queue.append(value)
                visited.add(value)
                parent[value]=currentNode
        # print(visited)
    return None



rule1=input("").split(" ")
rule2=input("").split(" ")
rule3=input("").split(" ")
steps,start,goal=tuple(input("").split(" "))
steps=int(steps)
# print(generateMoves("AAA"))
path=list(reversed(findPath(start,goal,steps)))
if path!=None:
    for a in path:
        print(f"{a[0]} {a[1]} {a[2]}")