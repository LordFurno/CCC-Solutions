n=int(input(""))
votes=list(str(input("")))
if votes.count("A")>votes.count("B"):
    print("A")
elif votes.count("B")>votes.count("A"):
    print("B")
else:
    print("Tie")