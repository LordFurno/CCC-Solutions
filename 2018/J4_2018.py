def convert(list1):#takes in a list of a list
    string=""
    for a in list1:
        string+=str(a)+" "
    return string
def check(list1):#Takes in a list within a list.
    columns=list(zip(*list1))
    run=True
    for a in columns:
        temp=list(a[:])
        temp.sort()
        if temp!=list(a):
            run=False
            break
    if run==True:
        for a in list1:
            temp=a[:]
            temp.sort()
            if temp==a:
                return True
            else:
                run=False
                break
    if run==False:
        return False

n=int(input(""))
rows=[]
for a in range(n):
    rows.append(list(map(int,input("").split(" "))))
columns=list(zip(*rows))
right90=list(map(list,map(reversed,columns)))
newColumns=list(zip(*right90))
right180=list(map(list,map(reversed,newColumns)))
newColumns=list(zip(*right180))
right270=list(map(list,map(reversed,newColumns)))
if check(rows)==True:
    for a in rows:
        print(convert(a))

elif check(right90)==True:
    for a in right90:
        print(convert(a))

elif check(right180)==True:
    for a in right180:
        print(convert(a))

elif check(right270)==True:
    for a in right270:
        print(convert(a))