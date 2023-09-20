n=int(input(""))
points=[]
for a in range(n):
    points.append(tuple(map(int,tuple(input("").split(",")))))
print(str(min(points,key=lambda x:x[0])[0]-1)+","+str(min(points,key=lambda x:x[1])[1]-1))
print(str(max(points,key=lambda x:x[0])[0]+1)+","+str(max(points,key=lambda x:x[1])[1]+1))