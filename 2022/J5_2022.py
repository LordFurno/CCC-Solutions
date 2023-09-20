import itertools
n=int(input(""))
t=int(input("")) 
trees=[]
border=[]
onlyTrees=[]
for i in range(n):#Adding the borders 0-15
    trees.append((0,i))
    trees.append((i,0))
    trees.append((n+1,i))
    trees.append((i,n+1))
    border.append((0,i))
    border.append((i,0))
    border.append((n+1,i))
    border.append((i,n+1))
trees=list(set(trees))
for i in range(t):
    value=tuple(map(int,input("").split(" ")))
    trees.append(value)
    onlyTrees.append(value)
# print(trees)
pairs=list(itertools.combinations(trees,2))#Generating all possilbe pairs, for some stupid reason doesn't pair the trees themselves. Wtf
treeCombos=list(itertools.combinations(onlyTrees,2))
for a in treeCombos:
    pairs.append(a)

# print(len(pairs))
counter=0
possibleSize=[]
for value in pairs:
    tree1=value[0]
    tree2=value[1]
    size=abs(tree1[1]-tree2[1])-1

    #If the size is smaller than the current max, then just don't do the calculations
    if size!=0 and (size!=n and t>0):
        horizontalLine=[]#Only the y coordinates
        leftTree=min(tree1,tree2,key=lambda x:x[1])
        rightTree=max(tree1,tree2,key=lambda x:x[1])
        for a in range(leftTree[1]+1,rightTree[1]):
            horizontalLine.append(a)
        
        searching=[]
        for obstacle in trees:        
            if obstacle[1] in horizontalLine:
                searching.append(obstacle)

        if len(searching)==0:
            possibleSize.append(size)
        else:
        # print(len(searching))
            otherSizes=[0]
            searching.sort(key=lambda x:abs(0-x[0]))
            xValues=list(zip(*searching))[0]
            newSize=0
            topPoint=min(searching,key=lambda x:x[0])
            lowPoint=max(searching,key=lambda x:x[0])
            for a in range(topPoint[0]+1,lowPoint[0]):
                if a in xValues:
                    otherSizes.append(newSize)
                    newSize=0
                else:
                    newSize+=1
                if a==lowPoint[0]-1:
                    otherSizes.append(newSize)
            if max(otherSizes)>=size:
                possibleSize.append(size)

        # if tree1 in onlyTrees and tree2 in onlyTrees and size==7:
        #   print(leftTree)
        #   print(rightTree)
        #   print(topPoint)
        #   print(lowPoint)
        #   print(otherSizes)
        #   print(xValues)
        #   print(size)
        #   print(searching)
        #   print("")
        #Need to calculate vertically, should be simple and very similar        
    # print(len(pairs))

    # print(trees)
print(max(possibleSize))
