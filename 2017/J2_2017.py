num=str(input(""))
k=int(input(""))
result=0
for i in range(k+1):
    result+=int(num)
    num+="0"
print(result)