import collections
def getMoves(value):#Could rewrite this cleaner
    possible=[]
    for index,el in enumerate(value):#Need to remeber to check for case where we are dealing with a stack of coins.
        if el!=None:
            if index!=len(value)-1 and index!=0:
                if value[index-1]==None:#If the space to the left is empty
                    temp=value[:]
                    temp[index-1]=int(str(el)[0])
                    if len(str(el))==1:
                        temp[index]=None
                    else:
                        temp[index]=int(str(el)[1:])
                    possible.append(temp)
                elif int(str(value[index-1])[0])>int(str(el)[0]):#If you can move the coin to the left onto a stack
                    temp=value[:]
                    temp[index-1]=int(str(el)[0] + str(value[index-1]))
                    if len(str(el))==1:
                        temp[index]=None
                    else:
                        temp[index]=int(str(el)[1:])
                    possible.append(temp)
                
                if value[index+1]==None:#If the space to the right is empty
                    temp=value[:]
                    temp[index+1]=int(str(el)[0])
                    if len(str(el))==1:
                        temp[index]=None
                    else:
                        temp[index]=int(str(el)[1:])
                    possible.append(temp)
                elif int(str(value[index+1])[0])>int(str(el)[0]):
                    temp=value[:]
                    temp[index+1]=int(str(el)[0] + str(value[index+1]))
                    if len(str(el))==1:
                        temp[index]=None
                    else:
                        temp[index]=int(str(el)[1:])
                    possible.append(temp)
            elif index==0:
                if value[index+1]==None:#If the space to the right is empty
                    temp=value[:]
                    temp[index+1]=int(str(el)[0])
                    if len(str(el))==1:
                        temp[index]=None
                    else:
                        temp[index]=int(str(el)[1:])
                    possible.append(temp)
                elif int(str(value[index+1])[0])>int(str(el)[0]):
                    temp=value[:]
                    temp[index+1]=int(str(el)[0] + str(value[index+1]))
                    if len(str(el))==1:
                        temp[index]=None
                    else:
                        temp[index]=int(str(el)[1:])
                    possible.append(temp)
            else:
                if value[index-1]==None:#If the space to the left is empty
                    temp=value[:]
                    temp[index-1]=int(str(el)[0])
                    if len(str(el))==1:
                        temp[index]=None
                    else:
                        temp[index]=int(str(el)[1:])
                    possible.append(temp)
                elif int(str(value[index-1])[0])>int(str(el)[0]):#If you can move the coin to the left onto a stack
                    temp=value[:]
                    temp[index-1]=int(str(el)[0] + str(value[index-1]))
                    if len(str(el))==1:
                        temp[index]=None
                    else:
                        temp[index]=int(str(el)[1:])
                    possible.append(temp)

    return possible



                       
                   
                
# print(getMoves([None,32,1])) 

def shortestPath(inital,goal):
    queue=collections.deque([tuple(inital)])
    visited=set([tuple(inital)])
    parent={tuple(inital):None}
    while len(queue)>0:
        current=queue.popleft()

        if list(current)==goal:   
            curPath=[current]
            while parent[current]!=None:
                current=parent[current]
                curPath.append(current)

            return list(reversed(curPath))
        possibleMoves=getMoves(list(current))#Gets the new positions
        for move in possibleMoves:
            if tuple(move) not in visited:
                queue.append(tuple(move))
                visited.add(tuple(move))
                parent[tuple(move)]=current
    # print(visited)
    
              
        

    

n=1
printing=[]
while n!=0:
    n=int(input(""))
    if n==0:
        break
    value=list(map(int,input("").split(" ")))
    goal=value[:]
    goal.sort()
    path=shortestPath(value,goal)
    if path==None:
        printing.append("IMPOSSIBLE")
    else:
        printing.append(len(path)-1)

    # print(getMoves(value))

for a in printing:
   print(a)