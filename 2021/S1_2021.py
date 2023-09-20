n=int(input(""))
heights=list(map(int,input("").split(" ")))
widths=list(map(int,input("").split(" ")))
calculate=[]
total=0
for i in range(len(heights)-1):
    calculate.append((heights[i],heights[i+1],widths[i]))
for a in calculate:
    if (a[0]+a[1])*a[2]%2==0:
        total+=int(((a[0]+a[1])*a[2])/2)
    else:
        total+=((a[0]+a[1])*a[2])/2
print(total)