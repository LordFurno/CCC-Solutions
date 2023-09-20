coordinates=[(0,-1),(0,-2),(0,-3),(1,-3),(2,-3),(3,-3),(3,-4),(3,-5),(4,-5),(5,-5),(5,-4),(5,-3),(6,-3),(7,-3),(7,-4),(7,-5),(7,-6),(7,-7),(6,-7),(5,-7),(4,-7),(3,-7),(2,-7),(1,-7),(0,-7),(-1,-7),(-1,-6),(-1,-5)]
commands=""
while "q" not in commands:
    commands=tuple(input("").split(" "))
    if commands[0]=="l":
        for i in range(int(commands[1])):
            current=coordinates[-1]
            temp=current[0]-1,current[1]
            coordinates.append(temp)
        
    elif commands[0]=="r":
        for i in range(int(commands[1])):
            current=coordinates[-1]
            temp=current[0]+1,current[1]
            coordinates.append(temp)
            

    elif commands[0]=="u":
        for i in range(int(commands[1])):
            current=coordinates[-1]
            temp=current[0],current[1]+1
            coordinates.append(temp)

    elif commands[0]=="d":
        for i in range(int(commands[1])):
            current=coordinates[-1]
            temp=current[0],current[1]-1
            coordinates.append(temp)
    elif commands[0]=="q":
        break
    if len(set(coordinates))!=len(coordinates):
        for a in coordinates:
            counter=coordinates.count(a)
            if counter>1:
                print(" ".join(map(str,coordinates[-1]))+" DANGER")
                break
    else:
        print(" ".join(map(str,coordinates[-1]))+" safe")