variables={"A":0,"B":0}
run=True
printing=[]
while run==True:
    command=input("").split(" ")
    if int(command[0])==1:
        variables[command[1]] = command[2]
    if int(command[0])==2:
        printing.append(variables[command[1]])
    if int(command[0])==3:
        variables[command[1]]=int(variables[command[1]])+int(variables[command[2]])
    if int(command[0])==4:
        variables[command[1]]=int(variables[command[1]])*int(variables[command[2]])
    if int(command[0])==5:
        variables[command[1]]=int(variables[command[1]])-int(variables[command[2]])
    if int(command[0])==6:
        variables[command[1]]=int(int(variables[command[1]])/int(variables[command[2]]))
    if int(command[0])==7:
        run=False
for a in printing:
    print(a)