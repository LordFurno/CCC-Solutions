n=int(input(""))
measurements=list(map(int,input("").split(" ")))
temp=measurements[:]
temp.sort(reverse=True)
maxes=temp
temp=measurements[:]
temp.sort()
lows=temp
# print(maxes)
# print(lows)
properOrder=[]
if n%2==0:#Max at end
    properOrder.append(maxes[0])
    maxes.pop(0)
    lows.pop(-1)
    while len(maxes)!=0 and len(lows)!=0:
        properOrder.append(lows[0])
        properOrder.append(maxes[0])
        if len(maxes)>2 and len(lows)>2:
            lows.pop(0)
            lows.pop(-1)
            maxes.pop(0)
            maxes.pop(-1)
        else:
            break
    properOrder.reverse()
    properOrder=list(dict.fromkeys(properOrder))
else:#Lowest at end
    lowest=lows[0]
    maxes.pop(-1)
    lows.pop(0)
    while len(maxes)!=0 and len(lows)!=0:
        properOrder.append(maxes[0])
        properOrder.append(lows[0])
        if len(maxes)>2 and len(lows)>2:
            lows.pop(0)
            lows.pop(-1)
            maxes.pop(0)
            maxes.pop(-1)
        else:
            break
    properOrder.reverse()
    properOrder.append(lowest)

    properOrder=list(dict.fromkeys(properOrder))#Maintains order while removing duplicates
    


for el in properOrder:
    print(el,end=" ")
    
# 8
# 10 50 40 7 3 110 90