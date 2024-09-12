score=input("Enter the scores of the studetns: ").split()
for i in range(0,len(score)):
    score[i]=int(score[i])
print(score)
high=score[0]
for j in range(1,len(score)):
    if high<score[j]:
        high=score[j]
print("The high score is ",high)