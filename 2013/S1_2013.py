year = int(input("")) + 1
temp = []
while True:
    temp = list(set(str(year)))
    length = len(str(year))
    if len(temp) >= length:
        print(year)
        break
    year += 1