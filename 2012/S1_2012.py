n=int(input(""))
combo=0
for a in range(1,n-2):
    secondSlot=(n-2)-a
    for c in range(a+1,n-1):
        for b in range(c+1,n):
            combo+=1
print(combo)