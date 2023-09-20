string1=list(input(""))
string2=list(input(""))

count=string2.count("*")
string1.sort()
string2.sort()
run=False
for value in string1:
  if value in string2:
    string2.remove(value)
  else:
    if count>0:
      count-=1
    else:
      print("N")
      run=True
      break
if run==False:
  print("A")