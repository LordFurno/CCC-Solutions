# import time

n=int(input(""))
# start=time.time()
dp=[[0]*n for a in range(n)]#For some reason list multiplication can get screwy.

sizes=list(map(int,input("").split(" ")))

for i in range(n):
    dp[i][i]=sizes[i]
for row in range(n-2,-1,-1):
    for col in range(row+1,n):
        if sizes[row]==sizes[col]:
            length=col-row +1#This is because 5,6 would still be considered 1
            if length==2:
               dp[row][col]=sizes[row]+sizes[col]
            elif length>=3:
                middleStart=row+1
                middleEnd=col-1
                if dp[middleStart][middleEnd]!=0:
                    dp[row][col]=sizes[row]+dp[middleStart][middleEnd]+sizes[col]
           
        else:#This is where all the time it takes comes from. This code here is slow
            searchCol = {dp[r][col] for r in range(n) if r >= row}#This is basically the zip but way faster. It gets the set of all the values in the column
            for value in dp[row]:
                if value!=0:
                    if value in searchCol:
                        index=dp[row].index(value)
                        otherIndex = [r for r in range(n) if dp[r][col] == value][0]#Gets the proper index, from the actual column. As getting the the index from the set wouldn't work
                        length=otherIndex-index +1#This is because 5,6 would still be considered 1
                        if length==2:
                            dp[row][col]=value*2

                        elif length>=3: 
                            middleStart=index+1
                            middleEnd=otherIndex-1
                            if dp[middleStart][middleEnd]!=0:
                                dp[row][col]=value*2+dp[middleStart][middleEnd]
           

            # print(searchCol)
 


#    print(row)
#    pass

# print(dp)
curMax=0
for row in dp:
    for val in row:
        if val>curMax:
           curMax=val
# end=time.time()
# print(end-start)
print(curMax)
'''
The logic for this problem is really cool. I use dynamic programming
I start by initalizing a matrix n x n

For the input:
7
47 12 12 3 9 9 3
  0  1  2  3  4  5  6
0
1
2
3
4
5
6
dp[r][c] represents the value of the combined riceballs from r to c. If it cannot be combined, the value is just 0.
Whenever r==c, the value in dp will simply be the riceball at r.
Starting from the bottom, you start filling this up.

If you are trying to combine something 4 or larger this is what happens:

If the first and last index are the same continue:
    first index=f
    last index=l

    Check the value in the dp array at dp[f-1][l-1], if it not equal to 0, then combine all 3 with this as the middle.

Once I finish filling up the entire dp matrix, I take the largest values found in the list, and apply them to the current lsit.
If there is possible combine, do it. I do this because for the sample input mentioned above, the dp array would end up being:
  0  1  2  3  4  5  6
0 47 0  0  0  0  0  0
1 0  12 24 0  0  0  0
2 0  0  12 0  0  0  0
3 0  0  0  3  0  0  24
4 0  0  0  0  9  18 0
5 0  0  0  0  0  9  0
6 0  0  0  0  0  0  3
We still need to combine 24.

This logic almost works:
I have to figure out how to deal with 20 20 20 20 4 60

To solve whenever you have a case like above, you simply get the column of the l index (in this case 60, which is 5)
Then search through that column and see it evere equals to something in the row of f. If it is combine them. You can
further optimize this by using sets as the column to check if the value is present, and then list comprehension to find
the index in the column

'''