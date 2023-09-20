import collections
def find(u,v,graph):
    queue=collections.deque([u])
    visited={u}
    while len(queue):
        curNode=queue.popleft()
        if curNode==v:
            return True#Connceted
        if curNode in graph:
            for neighbour in graph[curNode]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
    return False#Not connected


edges=[]
result={}
curPlan=[]
n,m,d=tuple(map(int,input("").split(" ")))
for l in range(m):

    a,b,c=tuple(map(int,input("").split(" ")))
    if l<=n-2:
        curPlan.append((c,a,b))
    edges.append((c,a,b))
edges.sort(key=lambda x:x[0])
parent={}
final=[]
counter=0
#Kruskal's algorithm, MST
for a in edges:
    # print(parent)
    if len(parent)==0:
        final.append(a)
        if a[1] not in parent:
            parent[a[1]]=[a[2]]
        else:
            temp=parent[a[1]]
            temp.append(a[2])

            parent[a[1]]=temp

        if a[2] not in parent:
            parent[a[2]]=[a[1]]
        else:
            temp=parent[a[2]]
            temp.append(a[1])
            parent[a[2]]=temp

    elif find(a[1],a[2],parent)==False:

        final.append(a)
        if a[1] not in parent:
            parent[a[1]]=[a[2]]
        else:
            temp=parent[a[1]]
            temp.append(a[2])

            parent[a[1]]=temp

        if a[2] not in parent:
            parent[a[2]]=[a[1]]
        else:
            temp=parent[a[2]]
            temp.append(a[1])
            parent[a[2]]=temp



if curPlan==final:
    print(0)
else:
    counter=0
    for a in final:
        if a not in curPlan:
            counter+=1
    print(counter)
    # print(len(curPlan)-len(final))
# print(final)
# print(curPlan)
# print(len(curPlan))
# print(final)
# print(m-len(final))
# print(final)