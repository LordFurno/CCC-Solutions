alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vowels=["a","e","i","o","u"]
indexes=[0,4,8,14,20]
string=str(input(""))
result=""
for a in string:
    if a in vowels:
        result+=a
    else:
        result+=a
        result+=alphabet[min(indexes, key=lambda x:abs(x-alphabet.index(a)))]
        if a!="z":
            for b in range(alphabet.index(a)+1,len(alphabet)):
                if alphabet[b] not in vowels:
                    result+=alphabet[b]
                    break
        else:
            result+="z"
print(result)