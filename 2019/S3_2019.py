row1=input("").split(" ")
row2=input("").split(" ")
row3=input("").split(" ")
grid=[]
grid.append(row1)
grid.append(row2)
grid.append(row3)
def check(grid):
    for a in range(3):
        if grid[a].count("X")>0:
            return False
    return True
while check(grid)==False:
    solutionRow={}
    rowDiff=[]
    colDiff=[]
    colCount=0
    rowCount=0
    for a in range(3):
        currentRow=grid[a] 
        if currentRow.count("X")==1:
            possibleIndexes=[0,1,2]#What this does is figure out which indexes holds the integers
            xIndex=currentRow.index("X")
            possibleIndexes.remove(xIndex)     
            if max(possibleIndexes)-min(possibleIndexes)>1:#In case x is in the middle
                rowDifference=int((int(currentRow[max(possibleIndexes)])-int(currentRow[min(possibleIndexes)]))/2)
            else:
                rowDifference=int(currentRow[max(possibleIndexes)])-int(currentRow[min(possibleIndexes)])#Calculates t he differences
            if xIndex!=0:#This fits in the new x value
                currentRow[xIndex]=int(currentRow[xIndex-1])+rowDifference
            else:
                currentRow[xIndex]=int(currentRow[1])-rowDifference
            solutionRow[a]=currentRow
            rowDiff.append(rowDifference)
        elif currentRow.count("X")==0:
            rowDifference=int(currentRow[1])-int(currentRow[0])
            rowDiff.append(rowDifference)
            rowCount+=1
        else:
            rowCount+=1      
    solutionCol={}
    for a in range(3):
        currentCol=list(list(zip(*grid))[a])   
        if currentCol.count("X")==1:
            possibleIndexes=[0,1,2]#What this does is figure out which indexes holds the integers
            xIndex=currentCol.index("X")
            possibleIndexes.remove(xIndex)       
            if max(possibleIndexes)-min(possibleIndexes)>1:#In case x is in the middle
                rowDifference=int((int(currentCol[max(possibleIndexes)])-int(currentCol[min(possibleIndexes)]))/2)
            else:
                rowDifference=int(currentCol[max(possibleIndexes)])-int(currentCol[min(possibleIndexes)])#Calculates t he differences
            if xIndex!=0:#This fits in the new x value
                currentCol[xIndex]=int(currentCol[xIndex-1])+rowDifference
            else:
                currentCol[xIndex]=int(currentCol[1])-rowDifference    
            solutionCol[a]=currentCol
            colDiff.append(rowDifference)
        elif currentCol.count("X")==0:
            rowDifference=int(currentCol[1])-int(currentCol[0])
            colDiff.append(rowDifference)
            colCount+=1
        else:
            colCount+=1
    #Code below combines the solved columns and rows
    newGrid=grid[:]
    for a in solutionRow.items():
        newGrid[a[0]]=a[1]
    for row in enumerate(newGrid):
        tempRow=list(row[1][:])
        for value in enumerate(row[1]):
            if value[1]=="X":
                if value[0] in solutionCol.keys():#If it solved the column
                    tempRow[value[0]]=solutionCol[value[0]][row[0]]
        newGrid[row[0]]=tempRow
    grid=newGrid
    if rowCount==3 and colCount==3:#The stupid edge case, where there are no possible ones that can be solved
        # print(rowDiff)
        if rowDiff!=[]:#I'm pretty sure, I need to cover columns too
            for row in enumerate(grid):#Does the rows
                tempRow=row[1][:]
                if row[1].count("X")>0:
                    # print(row[1])
                    for value in enumerate(row[1]):
                        if value[1]!="X":
                            index=value[0]
                            if index!=0:
                                tempRow[index-1]=int(row[1][index])-rowDiff[-1]
                            else:
                                tempRow[index+1]=int(row[1][index])+rowDiff[-1]
                            break
                    grid[row[0]]=tempRow
                    break
        elif colDiff!=[]:
            columns=list(map(list,list(zip(*grid))))
            solvedRow=[]
            for el in columns:
                if el.count("X")==0:
                    solvedRow=el
            for row in enumerate(columns):#Does the rows
                tempRow=row[1][:]
                if row[1].count("X")==0:
                    solvedRow=row[1]
                if row[1].count("X")>0:
                    if row[1].count("X")==3:
                        if solvedRow==[]:
                            tempRow=row[1]
                        else:
                            tempRow=solvedRow
                    else:
                        for value in enumerate(row[1]):
                            if value[1]!="X":
                                index=value[0]
                                if index!=0:
                                    tempRow[index-1]=int(row[1][index])-colDiff[-1]
                                else:
                                    tempRow[index+1]=int(row[1][index])+colDiff[-1]
                                break
                    columns[row[0]]=tempRow
            grid=list(zip(columns[0],columns[1],columns[2]))
            grid=list(map(list,grid))
        else:#If there is nothing solved
            xCounter=0
            types=[]
            for row in grid:
                for value in row:
                    if value=="X":
                        xCounter+=1
                    else:
                        types.append(int(value))
            if len(set(types))==1:
                xCounter=8
            if xCounter<=7:#If there are under 7 x's and none of them can be solved
                search=[]#Row, index in row, value
                run=True
                for row in enumerate(grid):
                    if run==False:
                        break
                    for value in enumerate(row[1]):
                        if value[1]!="X":#I know this is the only non x vlaue in this row. This also means this is the first time I find a value
                            search=[row[0],value[0],int(value[1])] 
                            prevRow=grid[search[0]-1]
                            for value in enumerate(prevRow):
                                if value[1]!="X":
                                    index=value[0]
                                    newValue=value
                                    addedValue=search[2]+int(newValue[1])
                                    if search[0]-1==-1:#If it connects to the end of the grid, then the newvalue has to be in the middle
                                        replaceRow=grid[1]
                                        if search[1]==2:
                                            for a in enumerate(replaceRow):
                                                if a[1]=="X":
                                                    replaceRow[a[0]]=addedValue
                                                    break
                                        else:
                                            replaceRow[index]=addedValue
                                        grid[1]=replaceRow
                                        
                                    else:
                                        replaceRow=grid[search[0]-1]
                                        if index==0:
                                            replaceRow[index+1]=addedValue
                                        else:
                                            replaceRow[index-1]=addedValue
                                        grid[search[0]-1]=replaceRow
                                    run=False
                                    break
                            break          
            if xCounter>=8:
                newValue=0
                for row in grid:
                    for value in row:
                        if value!="X":
                            newValue=value
                            break
                newRow=[newValue,newValue,newValue]
                grid[0]=newRow
                grid[1]=newRow
                grid[2]=newRow
for row in grid:
    rowString=""
    for value in row:
        rowString+=str(value)+" "
    print(rowString)