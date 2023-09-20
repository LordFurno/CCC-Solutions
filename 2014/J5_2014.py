n=int(input(""))
group1=input("").split(" ")
group2=input("").split(" ")
pair=[]
for a in range(len(group1)):
    pair.append((group1[a],group2[a]))
counter=0
for a in pair:
    if a[0]==a[1]:
        break
    for b in pair:
        if b[0]==a[1] and b[1]==a[0]:
            counter+=1
if counter==n:
    print("good")
else:
    print("bad")