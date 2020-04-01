score = [1,2,0,0,4,1,6,2,1,3]
sumscore = 0

scoreboard = {1:0, 2:0}
on, off = 1, 2
ball = 0
over = 0
n = 1
for i in score:
    ball += 1
    if i >= 0:
        scoreboard[on] += i
    if i % 2 == 1:
        on, off = off, on
    if ball == 6*n:
        n += 1
        on, off = off, on
        
for k in scoreboard:
    print('The score of batsman %d is: '%k)
    print(scoreboard[k])

for j in range(0, len(score)):    
   sumscore = sumscore + score[j];
     
print("The total score is: " + str(sumscore));