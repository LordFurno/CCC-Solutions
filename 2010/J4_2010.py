count=1
value=input("")
printing=[]
while value!="0":
    count=1
    '''
    Logic is super simple, get all indexes of the starting value, from there jump to each point see if it continues the pattern to find the length of pattern.
    
    '''
    value=list(map(int,value.split(" ")))[1:]
    diff=[value[i+1]-value[i] for i in range(len(value)-1)]
    indexes=[i for i,val in enumerate(diff) if val==diff[0]]#Possible starting points for other patterns
    # possible=[]
    if 0 in indexes:
        indexes.remove(0)
    indexes.sort()

    run=True
    for index in indexes:
        currentPattern=diff[0:index]
        if len(diff)-index<len(currentPattern):
            leftOver=diff[index:]
            if leftOver==currentPattern[0:len(leftOver)]:
                printing.append(len(currentPattern))
                run=False
                break
        else:
            leftOver=diff[index:]
            if len(leftOver)%len(currentPattern)==0:
                repeats=int(len(leftOver)/len(currentPattern))
                if currentPattern+currentPattern*repeats==diff:
                    printing.append(len(currentPattern))
                    run=False
                    break
            else:
                repeats=int(len(leftOver)/len(currentPattern))
                new=currentPattern+currentPattern*repeats
                leftOver=diff[len(new):]
                if leftOver==currentPattern[0:len(leftOver)]:
                    printing.append(len(currentPattern))
                    run=False
                    break
    if run==True:
        printing.append(len(diff))
    value=input("")
    if value=="0" or value=="0 ":
        break

for a in printing:
    print(a)