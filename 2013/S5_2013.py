import collections
import math
def findFactors(n):
    factors=set([])
    for a in range(1,int(math.sqrt(n))+1):
        if n%a==0:
            factors.add((a,int(n/a)))
            factors.add((int(n/a),a))
    factors=list(factors)
    return factors

n=int(input(""))
costs=[float('inf')] * (n+1)

costs[1]=0

for b in (range(1,len(costs))):
    factors=findFactors(b)
    for value in factors:
        newVal=b+value[0]
        newCost=costs[b]+value[1]
        if newVal<=n:
            if costs[newVal]>newCost:
                costs[newVal]=newCost
print(costs[n])