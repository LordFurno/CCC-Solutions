g=int(input(""))
p=int(input(""))
spots=[[True,0]]*(g+1)#True is open, False is closed
# print(spots)
end=""
check=True
for a in range(p):
    location=int(input(""))
    if spots[location][0]==True:
        spots[location]=[False,1]

    elif spots[location][0]==False:
        # print("HERE")
        newLocation=location-spots[location][1]
        if newLocation!=0 and spots[newLocation][0]==True:
            spots[newLocation]=[False,1]
            spots[location]=[False,spots[location][1]+1]
        elif spots[newLocation][0]==False:
            spots[newLocation]=[False,spots[newLocation][1]+1]
            spots[location]=[False,spots[location][1]+1]

            if check==True:#This is the stupid problem, that I have no idea how to fix, whatever approach I use, breaks everything else
                end=len(list(filter(lambda x:(x[0]==False),spots)))
                check=False

        if newLocation==0:
            if check==True:
                end=len(list(filter(lambda x:(x[0]==False),spots)))
                check=False
        # elif check==True:
        #     end=spots.count(False)
        #     check=False
if end!="":
    print(end)
else:
    print(len(list(filter(lambda x:(x[0]==False),spots))))
# print(spots[2000])
print(spots)
'''
The logic for this problem is as follows:
For each plane, I place it at the farthest gate possible. This allows for the maximum number of planes. 
If there is already a plane there, I add 1 to a counter, which counts how many times, I try and place a plane at that
location. With this counter, whenever I get calleed to the same location, I place the plane at location-counter. 

I find the spot to say the maximum planes can be placed by finding when I use the method above, and yet the spot is filled.
The problem is that, there might be another plane that has the maximum where I try and place it. So I should just move the plane down more. 

'''