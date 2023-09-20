start=tuple(map(int,input("").split(" ")))
end=tuple(map(int,input("").split(" ")))
chargeUnits=int(input(""))
shortest=abs(end[0]-start[0])+abs(end[1]-start[1])
if chargeUnits<shortest:
    print("N")
else:
    temp=chargeUnits-shortest
    if temp%2==0:
        print("Y")
    else:
        print("N")