repeat=int(input(""))
values=[]
for i in range(repeat):
    values.append(input(""))
for a in values:
    a=a.replace(" ","")
for a in values:
    temp=a.split()
    result=""
    for b in range(int(temp[0])):
        result+=str(temp[1])
    print(result)