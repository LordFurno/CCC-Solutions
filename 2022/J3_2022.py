numbers="1234567890"
value=list(input(""))
string=""
for a in enumerate(value):
    if a[1]!="-" and a[1]!="+" and a[1] not in numbers:
        string+=a[1]
    if a[1]=="+":
        tighten=""
        for b in range(a[0]+1,len(value)):
            if value[b] in numbers:
                tighten+=value[b]
            else:
                break
        print(string+" tighten "+tighten)
        string=""
    elif a[1]=="-":
        loosen=""
        for b in range(a[0]+1,len(value)):
            if value[b] in numbers:
                loosen+=value[b]
            else:
                break
        print(string+" loosen "+loosen)
        string=""