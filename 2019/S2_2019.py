n=int(input(""))
values=[]
for a in range(n):
    values.append(int(input(""))*2)

numbers=[]
primes=set([])

for i in range(2,max(values)):
    if i!=2 and i%2!=0:
        numbers.append(i)

while len(numbers)!=0:
    print(len(numbers))
    start=numbers[0]
    primes.add(start)
    numbers=list(filter(lambda x:(x%start!=0),numbers))

for a in values:
    for b in primes:
        if a-b in primes:
            print(str(b)+" "+str(a-b))
            break