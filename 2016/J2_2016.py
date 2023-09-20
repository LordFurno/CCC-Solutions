column={}
row1=input("")
row2=input("")
row3=input("")
row4=input("")
row1=row1.split()
row2=row2.split()
row3=row3.split()
row4=row4.split()
row1=[int(a) for a in row1]
row2=[int(a) for a in row2]
row3=[int(a) for a in row3]
row4=[int(a) for a in row4]
for a in range(len(row1)):
  result=0
  result+=row1[a]
  result+=row2[a]
  result+=row3[a]
  result+=row4[a]
  column[a]=result
total=[]
for a in column.values():
  total.append(a)
if sum(row1)==sum(row2)==sum(row3)==sum(row4):
  if len(set(total))==1:
    if total[0]==sum(row1):
      print("magic")
    else:
      print("not magic")
else:
  print("not magic")