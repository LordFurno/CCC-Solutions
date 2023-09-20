numbers=[1,2,3,4]
commands=input("")
for a in commands:
    if a=="H":
        numbers.insert(0,numbers[2])
        numbers.pop(3)
        numbers.insert(1,numbers[-1])
        numbers.pop(-1)
    if a=="V":
        numbers.insert(0,numbers[1])
        numbers.pop(2)
        numbers.insert(2,numbers[-1])
        numbers.pop(-1)
result=""
result+=str(numbers[0])+" "+str(numbers[1])
result+="\n"
result+=str(numbers[2])+" "+str(numbers[3])
print(result)