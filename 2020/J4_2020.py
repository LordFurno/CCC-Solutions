look=str(input(""))
shifts=[]
string=str(input(""))
shifts.append(string)
for a in range(len(string)):
    value=string[0]
    string=string[1:]
    string+=value
    shifts.append(string)
test=False
for a in shifts:
    if a in look:
        print("yes")
        test=True
        break
if test==False:
    print("no")