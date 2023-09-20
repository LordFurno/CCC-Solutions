import itertools
n=int(input(""))
k=int(input(""))
possilbe=[]
for i in range(1,n-(k-1)+1):
    possilbe.append(i)
test=list(itertools.combinations_with_replacement(possilbe,k))
counter=0
if k!=n:
    for a in test:
        temp=list(a[:])
        original=list(a[:])
        temp.sort()
        if temp==original and sum(original)==n:
            counter+=1
    print(counter)
else:
    print(1)