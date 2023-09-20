
t=int(input())
printing=[]
for a in range(t):
    n=int(input())
    cars=[]
    for b in range(n):
        cars.append(int(input()))
    cars.reverse()
    properOrder=cars[:]
    properOrder.sort()
    branch=[]
    counter=0
    lake=[]
    index=0
    while index<len(cars):
        value=cars[index]
        if value==properOrder[counter]:#If it is in the right order
            lake.append(value)
            # cars.remove(value)
            counter+=1
        else:
            if len(branch)>0:
                if branch[0]==properOrder[counter]:
                    lake.append(branch[0])
                    branch.pop(0)
                    index-=1
                    counter+=1
                else:
                    branch.insert(0,value)
            else:
                branch.insert(0,value)
        index+=1
    if len(branch)>0:
        for value in branch:
            if value==properOrder[counter]:
                lake.append(value)
                counter+=1
            else:
                break
    if lake==properOrder:
        printing.append("Y")
    else:
        printing.append("N")
        
for value in printing:
    print(value)