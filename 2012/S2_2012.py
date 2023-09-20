number=input("")
start=0
prevRoman=0
pairs=[]
mapping={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
temp=number[:]
while start+2<=len(number):
    curPair=number[start:start+2]
    pairs.append((int(curPair[0])*mapping[curPair[1]],mapping[curPair[1]]))
    start+=2
    temp=temp[2:]

if temp!="":
    if temp in list(mapping.keys()):
        pairs.append(mapping[temp])
    else:
        pairs.append(int(temp))
    
# print(temp)
for index,value in enumerate(pairs):
    if index!=len(pairs)-1:
        nextPair=pairs[index+1]
        if nextPair[1]>value[1]:
            pairs[index]=(-1*value[0],value[1])
print(sum(list(zip(*pairs))[0]))