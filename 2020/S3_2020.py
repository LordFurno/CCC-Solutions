def getFreq(value):
    freq={}
    for a in value:
        if a not in freq:
            freq[a]=1
        else:
            freq[a]+=1
    return freq
needle=input("")
haystack=input("")
needleFreq=getFreq(needle)


haystackFreq=getFreq(haystack[:len(needle)])

seen=set([])

# print(haystackFreq)
if haystackFreq==needleFreq:
    seen.add(haystack[:len(needle)])

for start in range(len(haystack)-len(needle)+1):

    current=haystack[start:len(needle)+start]#Current chunk
    if start!=0:
        newVal=haystack[start+len(needle)-1]#The new value from the chunk
        oldVal=haystack[start-1]#The old value to remove
        
        haystackFreq[oldVal]-=1

        if haystackFreq[oldVal]==0:
            del haystackFreq[oldVal]

        if newVal not in haystackFreq:
            haystackFreq[newVal]=1
        else:
            haystackFreq[newVal]+=1

        if haystackFreq==needleFreq:
            seen.add(current)
        
    
print(len(seen))