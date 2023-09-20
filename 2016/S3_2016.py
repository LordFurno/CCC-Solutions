import collections
def shortestPath(graph,goal,target):
    if goal==target:
        return 0
    queue=collections.deque([goal])
    visited=set([goal])
    parent={goal:None}
    while len(queue)>0:
        currentNode=queue.popleft()
        if currentNode==target:
            path=[currentNode]
            while parent[currentNode]!=None:
                currentNode=parent[currentNode]
                path.append(currentNode)
            return path
        for a in graph[currentNode]:
            if a not in visited:
                parent[a]=currentNode
                queue.append(a)
                visited.add(a)
                
    return -1
        
def findNearest(times,current,targets):
    currentLength=[]

    currentTimes=times[current]
    restruants=[]
    for pho in targets:
        restruants.append((pho,currentTimes[pho]))
    if len(restruants)==1:
        return restruants[0]
    else:
        temp=min(restruants,key=lambda x:x[1])
        return temp
        
 
	


    
n,m=tuple(map(int,input().split(" ")))
target=list(map(int,input().split(" ")))



road={}
for a in range(n-1):
	value=tuple(map(int,input().split(" ")))
	if value[0] in road.keys():
		temp=road[value[0]]
		if value[1] not in temp:
			temp.append(value[1])
		road[value[0]]=temp
	else:
		road[value[0]]=[value[1]]
  
	if value[1] in road.keys():
		temp=road[value[1]]
		if value[0] not in temp:
			temp.append(value[0])
			road[value[1]]=temp
	else:
		road[value[1]]=[value[0]]
times=[]
for a in range(-1,n-1):
    temp=[]
    for b in range(-1,n-1):
		#Finds the shortest path from node a to b
        path=shortestPath(road,a+1,b+1)
        if path!=0:
            temp.append(len(path)-1)
        else:
            temp.append(0)
    times.append(temp)
possibleTimes=[]
for start in target:
    total=0
    currentRest=target[:]
    currentRest.remove(start)
    cur=start
    while len(currentRest)>0:
        nextRest=findNearest(times,cur,currentRest)
        total+=nextRest[1]
        currentRest.remove(nextRest[0])
        cur=nextRest[0]
    possibleTimes.append(total)
    
    
print(min(possibleTimes))
# print(possibleTimes)
    


   
    
    
    # print(start)
    # print(restruants)
    # print(min(currentTimes,key=lambda x:(x in temp)))

# print(times)
# print(road)