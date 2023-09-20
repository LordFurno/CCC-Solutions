sides=[]
for i in range(3):
    sides.append(int(input("")))
if sum(sides)!=180:
    print("Error")
elif len(set(sides))==3:
    print("Scalene")
elif len(set(sides))==2:
    print("Isosceles")
else:
    print("Equilateral")