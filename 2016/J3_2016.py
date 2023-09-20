string=str(input(""))
string=list(string)
backward=list(reversed(string))
values=[]
if backward!=string:
  for start in range(len(string)):
    result=""
    for loop in range(start,len(string)):
      result+=string[loop]
      if list(result)==list(reversed(result)):
        values.append(result)
  final=[]
  for a in values:
    final.append(len(a))
  print(max(final))
elif backward==string:
  print(len(string))