numbers=[]
for i in range(4):
    numbers.append(int(input("")))
if numbers[0]!=9 and numbers[0]!=8:
    print("answer")
elif numbers[-1]!=9 and numbers[-1]!=8:
    print("answer")
elif numbers[1]!=numbers[2]:
    print("answer")
else:
    print('ignore')