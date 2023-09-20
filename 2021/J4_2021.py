order=list(str(input("")))
L=[]
M=[]
S=[]
proper=order[:]
proper.sort()
if order!=proper:
    for a in enumerate(proper):
        if order[a[0]]==proper[a[0]]:
            order[a[0]]=""
    order=list(filter(str,order))
    result=0
    proper=order[:]#This is to create a new duplicate list with the removed vallues, that is supposed to be the end result.
    proper.sort()
    while True:
        for a in enumerate(order):
            if a[1]=="L":
                L.append(a[0])
            elif a[1]=="M":
                M.append(a[0])
            elif a[1]=="S":
                S.append(a[0])
        if order==proper:
            break
        elif min(S)<max(L):#If L is after S
            order[max(L)]="S"
            order[min(S)]="L"
            result+=1
        elif min(S)<max(M):#If M is after S
            order[min(S)]="M"
            order[max(M)]="S"
            result+=1
    
        elif min(M)<max(L):#If M is after L
            order[min(M)]="L"
            order[max(L)]="M"
            result+=1
        L=[]
        M=[]
        S=[]
    print(result)
else:
    print("0")