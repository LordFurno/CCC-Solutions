distances=tuple(map(int,input("").split(" ")))
row=[]
row.append(0)
row.append(distances[0])
row.append(distances[0]+distances[1])
row.append(distances[0]+distances[1]+distances[2])
row.append(distances[0]+distances[1]+distances[2]+distances[3])
column=[]
column.append(0)
column.append(distances[0])
column.append(distances[0]+distances[1])
column.append(distances[0]+distances[1]+distances[2])
column.append(distances[0]+distances[1]+distances[2]+distances[3])

row2=[row[1]]
row2Constant=row[1]
row2.append(abs(row[1]-row2Constant))
row2.append(abs(row[2]-row2Constant))
row2.append(abs(row[3]-row2Constant))
row2.append(abs(row[4]-row2Constant))


row3=[row[2]]
row3Constant=row[2]
row3.append(abs(row[1]-row3Constant))
row3.append(abs(row[2]-row3Constant))
row3.append(abs(row[3]-row3Constant))
row3.append(abs(row[4]-row3Constant))


row4=[row[3]]
row4Constant=row[3]
row4.append(abs(row[1]-row4Constant))
row4.append(abs(row[2]-row4Constant))
row4.append(abs(row[3]-row4Constant))
row4.append(abs(row[4]-row4Constant))


row5=[row[4]]
row5Constant=row[4]
row5.append(abs(row[1]-row5Constant))
row5.append(abs(row[2]-row5Constant))
row5.append(abs(row[3]-row5Constant))
row5.append(abs(row[4]-row5Constant))


string=""
for a in row:
    string+=str(a)+" "
print(string)
string=""
for a in row2:
    string+=str(a)+" "
print(string)
string=""
for a in row3:
    string+=str(a)+" "
print(string)
string=""
for a in row4:
    string+=str(a)+" "
print(string)
string=""
for a in row5:
    string+=str(a)+" "
print(string)