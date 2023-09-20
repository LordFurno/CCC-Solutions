
import collections

def findShortest(graph,start,goals):
    visited=set([start])
    queue=collections.deque([start])
    parent={start:None}
    while len(queue)>0:
        currentNode=queue.popleft()
        if currentNode in goals:
            path=[currentNode]
            while parent[currentNode]!=None:
                currentNode=parent[currentNode]
                path.append(currentNode)
            return len(path)
        for neighbour in graph[currentNode]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                parent[neighbour]=currentNode
            
    

n=int(input(""))
linking={} 
reachedPages=[1]
ends=[]
for a in range(1,n+1):
    value=list(map(int,input("").split(" ")))
    if len(value)>1:
        linking[a]=value[1:]#Do I need the values as integers?
        # for a in value[1:]:
        #     reachedPages.append(a)
    else:
        ends.append(a)
        linking[a]=[]


    #1, 12, 84, 41
# print(linking)
short=findShortest(linking,1,ends)
reached=[1]
for value in list(map(list,linking.items())):
    temp=value[1]
    if value[0] in value[1]:
        temp.remove(value[0])
    reached+=temp
    # print(value)
# print(reached)
if len(set(reached))==n:
    print("Y")
else:
    print(f"N")
print(short)