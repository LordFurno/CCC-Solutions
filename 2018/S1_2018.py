n=int(input(""))
villages=[]
for a in range(n):
    villages.append(int(input("")))
distances=[]
for value in villages:
    temp=villages[:]
    minMax=(min(villages),max(villages))
    if value not in minMax:
        temp.remove(value)
        village1=min(temp,key=lambda x:abs(x-value))
        temp.remove(village1)
        village2=min(temp,key=lambda x:abs(x-value))
        if village1>value:
            while village2>value:
                temp.remove(village2)
                village2=min(temp,key=lambda x:abs(x-value))
        else:
            while village2<value:
                temp.remove(village2)
                village2=min(temp,key=lambda x:abs(x-value))
        distances.append(abs(((value+village1)/2)-((value+village2)/2)))
print(min(distances))