#Honestly, not 100% sure how everything works here but it does. The way it finds the optimal number is kind of confusing
#Every unique number at position k, will add k more good subsets
#Every non-unique number at position k will add the number of different values between most recent and k.
n,m,k=tuple(map(int,input("").split(" ")))
final=[]
for i in range(n):
    remaining=n-i-1#Number of spacecs left
    curVal=k-remaining#number of good subsets left for the remaining spots. 
    choice=min(curVal,m)#This is used to find whether we want a distinct or duplicate value. If m is greater than curval, it means that we can still have more unique values
    if choice<=0:
        break
    if choice>i:#Chose unique
        val=min(m,i+1)
        choice=val
    else:
        val=final[i-choice]
    final.append(val)
    k-=choice

if k<=0 and len(final)==n:
    print(" ".join(list(map(str,final))))
else:
    print(-1)