j=int(input(""))
a=int(input(""))
jerseys={}
counter=0
for b in range(1,j+1):
    value=input("")
    jerseys[b]=value

for b in range(a):
    need=input().split(" ")

    num=int(need[1])
    if num in jerseys.keys():
        if jerseys[num]==need[0]:
            counter+=1
            del jerseys[num]
        else:
            size=need[0]
            if size=="S":
                if jerseys[num]=="M" or jerseys[num]=="L":
                    counter+=1
                    del jerseys[num]
            elif size=="M":
                if jerseys[num]=="L":
                    counter+=1
                    del jerseys[num]

# print(jerseys)
print(counter)