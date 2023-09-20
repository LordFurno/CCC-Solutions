import time
import sys
def getFrequency(boards):
    freq = {}
    for value in boards:
        freq[value] = freq.get(value, 0) + 1#Use .get() so if it isn't in frequency, just set it to 1.
    return freq
start=time.time()
n=int(input(""))

boards=list(map(int, input("").split(" ")))


# boards=[]
# for a in range(100000):
#     print(a)
#     boards.append(1999)
sortedBoards=boards[:]
sortedBoards.sort()

# print(sortedBoards)

original=getFrequency(boards)

testing=[]
test={}
for a in range(4000,0,-1):#Literally just searches through possible sums for board pairs, sees how long the fence is records it. So it knows how many possible heights there can be for that fence length
    if sortedBoards[-1]+sortedBoards[-2]>=a:#Might be able to optimize here
        possibleSum=a
        longest=0
        start=time.time()
        freq=original.copy()#I do this because its faster
        for value in freq.keys():#Optimized code to find board combinations that add up to the sum
            if value>possibleSum:
                continue
            if freq[value]==0:
                continue

            match=possibleSum-value
            if match==value:
                numPairs=freq[match]//2
                longest+=numPairs
                freq[value]=freq[value]-numPairs*2
                freq[match]=freq[match]-numPairs*2

            elif match in freq.keys():
                if freq[match]>0:
                    numPairs=min(freq[match],freq[value])
                    longest+=numPairs
                    freq[match]=freq[match]-numPairs
                    freq[value]=freq[value]-numPairs
                    
        if longest not in test.keys():
            test[longest]=1
        else:
            test[longest]=test[longest]+1
    
output=max(test.items(),key=lambda x:x[0])
if output[0]==1:
    print(f"{output[0]} {sum(range(n))}")
else:
    print(f"{output[0]} {output[1]}")
# print(test)
# print(time.time()-start)
# print(sortedBoards)
