num=int(input(""))
possible=[]
counter=0
if num<=5:
    counter+=1
for i in range(1,num):
    x,y=i,num-i
    if y>x and y<=5 and x<=5:
        possible.append((y,x))
    if x>y and y<=5 and x<=5:
        possible.append((x,y))
    if x==y and y<=5 and x<=5:
        possible.append((x,y))
        
print(len(set(possible))+counter)