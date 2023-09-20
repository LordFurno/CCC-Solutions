p=int(input(""))
n=int(input(""))
r=int(input(""))
total=n
counter=0
while total<=p:
    total+=n*r
    n=n*r
    counter+=1
print(counter)