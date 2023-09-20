counter=0
N=int(input(""))
day1=list(input(""))
day2=list(input(""))
for a in range(len(day1)):
    if day2[a]==day1[a] and day1[a]!=".":
        counter+=1
print(counter)