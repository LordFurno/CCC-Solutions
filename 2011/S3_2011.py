def withinRange(x,y,m):#Finds the blocky range of the image, which is m
    if m==1:
        if (x>=1 and x<=3) and y==0:
            return True
        if x==2 and y==1:
            return True
        return False
    size=5**m
    if (x>=0.2*size and x<=0.2*size*4) and y<=5**(m-1)-1:
        return True
    if (x>=0.2*size*2 and x<=0.2*size*3) and y<=(5**(m-1))*2-1:
        return True
    return False
printing=[]
values=[]
t=int(input(""))
for a in range(t):
    values.append(tuple(map(int,input("").split(" "))))
    

for a in range(len(values)):
    found=False
    m,x,y=values[a]
    gridSize=5**m
    if withinRange(x,y,m):#If the location is in the inital blocks
        print("crystal")
    elif x<0.2*gridSize or x>0.2*gridSize*4:#Completley out of bounds
        print("empty")
    else:
        tempY=y
        tempX=x
        for b in range(m-1,0,-1):#What this code does is that, for each self-repeating section of the tip of the crystal, it scales the coordinates down, and the grid down to check that it would fit within that crystal. It does this for all smaller slef-repeating chunks
            #We need to scale down the coordinates to fit in magnification level of b
            for mod in range(b):
                if tempY-5**b>=0:
                    tempY-=5**b
                if tempX-5**b>=0:
                    tempX-=5**b
            if withinRange(tempX,tempY,b)==True:
                print("crystal")
                found=True
                break
        if found==False:
            print("empty")
# print(values)
