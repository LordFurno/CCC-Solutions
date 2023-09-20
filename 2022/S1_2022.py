n=int(input(""))
combos=0
temp=n

while temp>0:
    if temp%4==0:
        # temp-=4
        combos+=1
    temp-=5
if n%5==0:
    combos+=1

print(combos)