n=int(input(""))
computers={}
for a in range(n):
    value=list(input("").split(" "))
    value[1]=int(value[1])
    value[2]=int(value[2])
    value[3]=int(value[3])
    computers[value[0]]=2*value[1] + 3*value[2] + value[3]


computers=list(computers.items())
computers.sort(key=lambda x:x[1],reverse=True)
if len(computers)>0:
    if len(computers)>1:
        if computers[1][1]==computers[0][1]:
            temp=[computers[1],computers[0]]
            temp.sort(key=lambda x:x[0])
            print(temp[0][0])
            print(temp[-1][0])
        else:
            print(computers[0][0])
            print(computers[1][0])
    else:
        print(computers[0][0])