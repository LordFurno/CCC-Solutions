word = str(input(""))
flip = ["I", "O", "S", "H", "Z", "X", "N"]
counter=0
for a in word:
  if a in flip:
    counter+=1
if counter==len(word):
  print("YES")
else:
  print("NO")