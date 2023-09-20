n=int(input(""))
counter=0
student=[]
correct=[]
for a in range(n):
    student.append(input(""))
for a in range(n):
    correct.append(input(""))
for index,answer in enumerate(correct):
    if answer==student[index]:
        counter+=1
print(counter)