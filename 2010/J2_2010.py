#Tristan
a=int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))
s=int(input(""))
dupeS=s
steps=[]
while s!=0:
    if s<a:
        steps.append(s)
        s-=s
        break
    else:
        s-=a
        steps.append(a)
    if s<b:
        steps.append(s*-1)
        s-=s
        break
    else:
        s-=b
        steps.append(b*-1)
nikky=sum(steps)
steps=[]
while dupeS!=0:
    if dupeS<c:
        steps.append(dupeS)
        dupeS-=dupeS
        break
    else:
        dupeS-=c
        steps.append(c)
    if dupeS<d:
        steps.append(dupeS*-1)
        dupeS-=dupeS
        break
    else:
        dupeS-=d
        steps.append(d*-1)
byron=sum(steps)
if byron>nikky:
    print("Byron")
elif nikky>byron:
    print("Nikky")
else:
    print("Tied")