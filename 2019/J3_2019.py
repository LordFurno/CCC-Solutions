repeat=int(input(""))
values=[]
for a in range(repeat):
    values.append(input(""))
for i in values:
    temp=[]
    result=""
    while i!="":
        value=i[0]
        counter=0
        for a in i:
            if a==value:
                counter+=1
                i=i.replace(a,"")
        temp.append(str(counter)+" " + str(value)+" ")
    for a in temp:
        result+=a
    print(result[:-1])