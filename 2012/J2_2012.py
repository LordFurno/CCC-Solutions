numbers=[]
for i in range(4):
    numbers.append(int(input("")))
if numbers[3]>numbers[2]>numbers[1]>numbers[0]:
    print("Fish Rising")
elif numbers[0]>numbers[1]>numbers[2]>numbers[3]:
    print("Fish Diving")
elif numbers[0]==numbers[1]==numbers[2]==numbers[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")