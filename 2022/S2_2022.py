x=int(input(""))
same={}
for a in range(x):
    value=input("").split(" ")
    if value[0] in same:
        temp=same[value[0]]
        temp.append(value[1])
        same[value[0]]=temp
    else:
        same[value[0]]=[value[1]]

y=int(input(""))
diff={}
for a in range(y):
    value=input("").split(" ")
    if value[0] in diff:
        temp=diff[value[0]]
        temp.append(value[1])
        diff[value[0]]=temp
    else:
        diff[value[0]]=[value[1]]
g=int(input(""))
groups=[]
counter=0
for a in range(g):
    group=input("").split(" ")
    for person in group:
        if person in diff:
            for no in diff[person]:
                if no in group:

                    counter+=1
                    

        if person in same:
            for yes in same[person]:
                if yes not in group:

                    counter+=1
                    

print(counter)
