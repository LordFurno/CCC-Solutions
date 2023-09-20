import heapq
def shortest(graph,start,k):
    dist={node:[float('inf')] for node in graph}
    dist[start]=[(0,k)]
    pq=[(start,0,k)]#Node,weight,hull
    testCount=0
    while len(pq)>0:
        # testCount+=1

        # if testCount==6:
        #     break
        curNode,curWeight,curK=heapq.heappop(pq)
        check=()
        for a in dist[curNode]:
            if a[1]==curK:
                check=a
                break
        if check!=():
            if curWeight>check[0]:
                continue
        if graph[curNode]==None: #I don't know about this
            continue
        for value in graph[curNode].items():
            neighbor=value[0]
            for el in value[1]:
                
                weight=el[0]
                hull=el[1]
                newWeight=weight+curWeight
                newHull=curK-hull
                check=True
                if newHull>0:
                    length=len(pq)
                    for i,a in enumerate(dist[neighbor]):
                        if a==float('inf'):
                            dist[neighbor]=[(newWeight,newHull)]
                            heapq.heappush(pq,(neighbor,newWeight,newHull))
                            break
                        elif a[1]==newHull and newWeight<a[0]:
                            # print("HERE")
                            # print(dist[neighbor])
                            temp2=dist[neighbor].copy()
                            temp2[i]=(newWeight,newHull)
                            dist[neighbor]=temp2
                            # print(dist[neighbor])
                            heapq.heappush(pq,(neighbor,newWeight,newHull))
                            break
                        elif a[1]==newHull and newWeight>a[0]:
                            check=False
                    if len(pq)==length and check==True:
                        temp=dist[neighbor]
                        temp.append((newWeight,newHull))
                        dist[neighbor]=temp
                        heapq.heappush(pq,(neighbor,newWeight,newHull))

            
                        
                

    return dist

graph={}
k,n,m=tuple(map(int,input("").split(" ")))
# print(k)
for a in range(m):
    value=tuple(map(int,input("").split(" ")))
    if value[0] not in graph:
        graph[value[0]]={value[1]:[(value[2],value[3])]}
    else:
        curGraph=graph[value[0]]
        if value[1] in curGraph:
            temp=curGraph[value[1]]
            temp.append((value[2],value[3]))
            curGraph[value[1]]=temp
            graph[value[0]]=curGraph
        else:
            curGraph[value[1]]=[(value[2],value[3])]
            graph[value[0]]=curGraph
        
    if value[1] not in graph:
        graph[value[1]]={value[0]:[(value[2],value[3])]}
    else:
        curGraph=graph[value[1]]
        if value[0] in curGraph:
            temp=curGraph[value[0]]
            temp.append((value[2],value[3]))
            curGraph[value[0]]=temp
            graph[value[1]]=curGraph
        else:
            curGraph[value[0]]=[(value[2],value[3])]
            graph[value[1]]=curGraph


# print(graph)
a,b=tuple(map(int,input("").split(" ")))
solution=shortest(graph,a,k)
# print(solution)
solution=solution[b]
# print(shortest(graph,a,k))
if solution==[float('inf')]:
    print(-1)
else:
    solution.sort(key=lambda x:x[0])
    check=False
    for a in solution:
        if a[1]>0 and a[1]<=k:
            print(a[0])
            check=True
            break
    if check==False:
        print(-1)
# print(solution)
# print(graph)