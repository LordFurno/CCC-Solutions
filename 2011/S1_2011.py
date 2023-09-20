n=int(input(""))
t=0
s=0
for a in range(n):
    line=list(input(""))
    for char in line:
        if char.lower()=="t":
            t+=1
        elif char.lower()=="s":
            s+=1
if s==t:
    print("French")
elif s>t:
    print("French")
else:
    print("English")
