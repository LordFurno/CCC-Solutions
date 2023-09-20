t1=int(input(""))
t2=int(input(""))
counter=0
while t1-t2>=0:
    temp=t2
    t2=t1-t2
    t1=temp
    counter+=1
print(counter+2)