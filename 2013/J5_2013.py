import itertools
def win(combo,fav,teams,scores):
    tempScores=scores.copy()
    for index,team in enumerate(combo):
        if team[0]=="T":
            currentTeam=teams[index]
            tempScores[currentTeam[0]]=tempScores[currentTeam[0]]+1
            tempScores[currentTeam[1]]=tempScores[currentTeam[1]]+1
        elif team[0]=="W":
            currentTeam=teams[index][0]
            tempScores[currentTeam]=tempScores[currentTeam]+3
        elif team[1]=="W":
            currentTeam=teams[index][1]
            tempScores[currentTeam]=tempScores[currentTeam]+3
        
                
    top=list(tempScores.items())
    top.sort(key=lambda x:x[1],reverse=True)
    if top[0][0]==fav and top[1][1]<top[0][1]:
        return True
    return False
            
                


t=int(input())
g=int(input())
teams=[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
scores={1:0,2:0,3:0,4:0}
games=[]
for a in range(g):
    value=list(map(int,input().split(" ")))
    if value[2]>value[3]:#Team A won
        scores[value[0]]=scores[value[0]]+3
    elif value[3]>value[2]:#Team B won
        scores[value[1]]=scores[value[1]]+3
    elif value[3]==value[2]:
        scores[value[1]]=scores[value[1]]+1
        scores[value[0]]=scores[value[0]]+1
    games.append(value)
    if (value[0],value[1]) in teams:
        teams.remove((value[0],value[1]))
    elif (value[1],value[0]) in teams:
        teams.remove((value[1],value[0]))


        
# print(teams)
length=len(teams)
possibleCombos=list(itertools.product([(0,"W"),("W",0),("T","T"),],repeat=length))
# print(possibleCombos[0])
# print(teams)
counter=0
for value in possibleCombos:
    if win(value,t,teams,scores)==True:
        counter+=1
        # print(value)
        
print(counter)
# print(possibleCombos)
