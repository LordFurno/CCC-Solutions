#-O, O, -A, A, -B, B, -AB, AB 
units=list(map(int,input("").split(" ")))
people=list(map(int,input("").split(" ")))
maxPeople=0
for index,unit in enumerate(units):#Gives ouot the native blood
    if unit>people[index]:
        units[index]=unit-people[index]
        maxPeople+=people[index]
        people[index]=0
    else:
        maxPeople+=units[index]
        people[index]=people[index]-units[index]
        units[index]=0
negatives=[0,2,4,6]
positives=[1,3,5,7]
oNeg=units[0]
oPos=units[1]
for index,need in enumerate(people):#Gives out the O blood
    # need=people[index]
    if index in negatives and need>0:
        if oNeg>need:
            maxPeople+=need
            oNeg-=need
            people[index]=0
        else:
            people[index]=need-oNeg
            maxPeople+=oNeg
            oNeg=0
    elif index in positives and need>0:  
        if oPos>need:
            oPos-=need
            people[index]=0
            maxPeople+=need
        else:
            people[index]=need-oPos
            maxPeople+=oPos
            oPos=0
        temp=people[index]
        if oNeg>temp:
            maxPeople+=temp
            oNeg-=temp
            people[index]=0
        else:
            people[index]=temp-oNeg
            maxPeople+=oNeg
            oNeg=0      
units[0]=oNeg
units[1]=oPos
for index,unit in enumerate(units):#Gives leftover to AB
    if unit!=0:
        if people[6]>0 and index in negatives:
            if unit>people[6]:
                maxPeople+=people[6]
                units[index]=unit-people[6]
                people[6]=0
            else:
                maxPeople+=unit
                people[6]=people[6]-units[index]
                units[index]=0
        elif people[7]>0:
            if unit>people[7]:
                maxPeople+=people[7]
                units[index]=unit-people[7]
                people[7]=0
            else:
                maxPeople+=unit
                people[7]=people[7]-units[index]
                units[index]=0
for index,need in enumerate(people):
    if index in positives and need>0:
        prev=units[index-1]
        if prev>need:
            maxPeople+=need
            people[index]=0
            units[index-1]=prev-need
        elif need>prev:
            maxPeople+=prev
            people[index]=people[index]-prev
            units[index-1]=0

# print(units)
# print(people)
print(maxPeople)