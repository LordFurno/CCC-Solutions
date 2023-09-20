question=int(input(""))
N=int(input(""))
town1=input("")
town2=input("")
dmo=[]
peg=[]
word=""
counter=0
for a in town1:
  counter+=1
  if a!=" ":
    word+=a
  if a==" " or counter==len(town1):
    dmo.append(word)
    word=""
counter=0
for a in town2:
  counter+=1
  if a!=" ":
    word+=a
  if a==" " or counter==len(town2):
    peg.append(word)
    word=""
answer=0
dmo=[int(a) for a in dmo]
peg=[int(a) for a in peg]
if question==1:
  while len(dmo)!=0:
    total=[]
    total.append(max(dmo))
    total.append(max(peg))
    dmo.remove(max(dmo))
    peg.remove(max(peg))
    answer+=int(max(total))
  print(answer)
if question==2:
  while len(dmo)!=0:
    a=(int(max(dmo)),int(min(peg)))
    answer+=int(max(a))
    dmo.remove(a[0])
    peg.remove(a[1])
  print(answer)