n=int(input(""))
good_players=0
for i in range(n):
    stars=0
    points=int(input(""))
    fouls=int(input(""))
    stars+=points*5
    stars-=fouls*3
    if stars>40:
        good_players+=1
if n==good_players:
    print(str(good_players)+"+")
else:
    print(good_players)