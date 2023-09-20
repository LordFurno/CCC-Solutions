import collections


def possibleJumps(pos):
    jumps=[]

    temp=[pos[0]+1,pos[1]+2]#1 right 2 up
    if (temp[0]<=8 and temp[1]<=8) and (temp[0]>0 and temp[1]>0):
        jumps.append(tuple(temp))

    temp=[pos[0]-1,pos[1]+2]#1 left 2 up
    if (temp[0]<=8 and temp[1]<=8) and (temp[0]>0 and temp[1]>0):
        jumps.append(tuple(temp))

    temp=[pos[0]+2,pos[1]+1]#2 right 1 up
    if (temp[0]<=8 and temp[1]<=8) and (temp[0]>0 and temp[1]>0):
        jumps.append(tuple(temp))

    temp=[pos[0]-2,pos[1]+1]#2 left 1 up
    if (temp[0]<=8 and temp[1]<=8) and (temp[0]>0 and temp[1]>0):
        jumps.append(tuple(temp))

    temp=[pos[0]-2,pos[1]-1]#2 left 1 down
    if (temp[0]<=8 and temp[1]<=8) and (temp[0]>0 and temp[1]>0):
        jumps.append(tuple(temp))

    temp=[pos[0]+2,pos[1]-1]#2 right 1 down
    if (temp[0]<=8 and temp[1]<=8) and (temp[0]>0 and temp[1]>0):
        jumps.append(tuple(temp))

    temp=[pos[0]+1,pos[1]-2]#1 right 2 down
    if (temp[0]<=8 and temp[1]<=8) and (temp[0]>0 and temp[1]>0):
        jumps.append(tuple(temp))

    temp=[pos[0]-1,pos[1]-2]#1 left 2 down
    if (temp[0]<=8 and temp[1]<=8) and (temp[0]>0 and temp[1]>0):
        jumps.append(tuple(temp))
    return jumps


def search(start,target):
    queue=collections.deque([start])
    visisted=set([start])
    parent={start:None}
    while len(queue)>0:
        currentNode=queue.popleft()
        if currentNode==target:
            path=[currentNode]
            while parent[currentNode]!=None:
                currentNode=parent[currentNode]
                path.append(currentNode)
            return path
            
        possible=possibleJumps(currentNode)
        for a in possible:
            if a not in visisted:
                queue.append(a)
                visisted.add(a)
                parent[a]=currentNode

                
start=tuple(map(int,input("").split(" ")))
end=tuple(map(int,input("").split(" ")))
print(len(search(start,end))-1)