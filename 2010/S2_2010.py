n = int(input(""))
rule = []
for i in range(n):
    rule.append(tuple(input("").split(" ")))
decode = input("")
rule.sort(key=lambda x: len(x[1]))
rule.reverse()
result = ""
while True:
    if len(decode) == 0:
        break
    for a in rule:
        length = len(a[1])
        check = decode[0:length]
        if check == a[1]:
            result += str(a[0])
            decode = decode[length:]
print(result)