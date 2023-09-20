a1=int(input(""))
a2=int(input(""))
a3=int(input(""))
b1=int(input(""))
b2=int(input(""))
b3=int(input(""))
a_sum=a1*3+a2*2+a3
b_sum=b1*3+b2*2+b3
if a_sum>b_sum:
    print("A")
elif b_sum>a_sum:
    print("B")
elif b_sum==a_sum:
    print("T")