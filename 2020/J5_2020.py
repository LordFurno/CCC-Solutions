import collections



def findPath(grid,startValue,goalValue,startLocation):
    queue=collections.deque([(startValue,startLocation[0],startLocation[1])])
    visited=set([(startValue,startLocation[0],startLocation[1])])
    while len(queue)>0:
        # print(queue)
        currentNode=queue.popleft()
        if currentNode[0]==goalValue:
            return "yes"
        
        newValue=currentNode[1]*currentNode[2]
        if newValue in locations.keys():
            
            indexes=locations[newValue]

            for el in indexes:
                temp=(newValue,el[0],el[1])
                if temp not in visited:
                    if el[0]*el[1]==goalValue:
                        return "yes"
                    queue.append(temp)
                    visited.add(temp)

    # print(visited)
    return None
        
# import time

m=int(input(""))
n=int(input(""))     
grid=[]      
locations={}

for a in range(m):
    grid.append(list(map(int,input("").split(" "))))

for rowIndex ,row in enumerate(grid):
    for colIndex,v in enumerate(row):
        if v not in locations:
            locations[v]=[(rowIndex+1,colIndex+1)]
        else:
            temp=locations[v]
            temp.append((rowIndex+1,colIndex+1))
            locations[v]=temp
# print(locations)
# start=time.time()
# print(findPath(grid,3,2,(2,2)))
if findPath(grid,m*n,grid[0][0],(m,n))!=None:
    print("yes")
else:
    print("no")
# end=time.time()
# print(end-start)