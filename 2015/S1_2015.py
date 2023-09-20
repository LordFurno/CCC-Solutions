k=int(input(""))
numbers=[]
for a in range(k):
    num=int(input())
    if num!=0:
        numbers.append(num)
    else:
        numbers.pop(-1)
print(sum(numbers))