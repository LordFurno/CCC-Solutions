def secondLargest(arr,maxVal):
    new=list(filter(lambda a: a[0] != maxVal, arr))
    new.sort(key=lambda x:x[0],reverse=True)
    return new[0][0]



def listCreator(original,value):
    newList=[]
    for el in original:
        if el[0]==value:
            newList.append(el)
    return newList
n=int(input(""))
readings=[]
final=0
for a in range(n):
    readings.append(int(input("")))

counter={}
for value in readings:
    counter[value]=counter.get(value,0)+1#.get, gets the value, if it doesn't exsist, returns 0

counts=[]
for val,count in counter.items():
    counts.append((count,val))#Count, value
counts.sort(key=lambda x:x[0],reverse=True)

highestFrequency=counts[0][0]

#1 of the highest frequency, and tied second-highest
if counts[1][0]<counts[0][0]:
    if counts[1][0]==counts[2][0]:
        secondHighest=secondLargest(counts,highestFrequency)
        tempList=listCreator(counts,secondHighest)
        tempList.sort(key=lambda x:abs(counts[0][1]-x[1]),reverse=True)#Sorts based on the largest absolute difference
        final=abs(counts[0][1]-tempList[0][1])
    else:
        final=abs(counts[0][1]-counts[1][1])
    

#3 or more of the highest frequency
elif counts[0][0]==counts[1][0] and counts[0][0]==counts[2][0]:
    tempList=listCreator(counts,highestFrequency)
    tempList.sort(key=lambda x:x[1],reverse=True)
    final=abs(tempList[0][1]-tempList[-1][1])
    
#2 of the Highest frequency, normal case
elif counts[0][0]==counts[1][0]:
    tempList=counts[:2]
    final=abs(tempList[0][1]-tempList[1][1])
else:
    final=abs(counts[0][1]-counts[1][1])

# print(counts)
print(final)
