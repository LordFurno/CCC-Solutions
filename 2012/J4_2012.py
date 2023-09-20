k = int(input(""))
decode = str(input(""))
result = ""
alphabet = ["A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
counter=0
for a in decode:
    p = counter + 1
    shift = 3 * p + k
    result += alphabet[alphabet.index(a) - shift]
    counter+=1  
print(result)