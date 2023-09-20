string=str(input(""))
aCounter=string.count("A")
bCounter=string.count("B")
cCounter=string.count("C")
windowSize=min(aCounter,bCounter)

if aCounter<bCounter:
    search="A"
elif aCounter>bCounter:
    search="B"
else:
    if aCounter==bCounter:
        search="A"

for poi in range(len(string)):
    if string[0]==string[-1]:
        string=string[1:]+string[0]
    else:
        break

window=string[0:windowSize]
counts=[]
testCounts=[]
for a in range(windowSize,len(string)):
    count=window.count(search)
    counts.append(count)
    window=window[1:]
    window+=string[a]
    if a==len(string)-1:
        count=window.count(search)
        counts.append(count)
        break

if len(counts)!=0:
    minCount=windowSize-max(counts)
    windowSize=max(aCounter,bCounter)

    if aCounter>bCounter:
        search="A"
    elif aCounter<bCounter:
        search="B"
    else:
        if aCounter==bCounter:
            search="A"
    
    window=string[0:windowSize]
    counts=[]
    # print(window)
    for a in range(windowSize,len(string)):
        count=window.count(search)
        counts.append(count)
        window=window[1:]
        window+=string[a]
        if a==len(string)-1:
            count=window.count(search)
            counts.append(count)
            break
    if len(counts)!=0:
        maxCount=windowSize-max(counts)
        print(min(maxCount,minCount))
    else:
        print(0)

else:
    print(0)

