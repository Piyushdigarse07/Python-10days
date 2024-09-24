# Nobita game scor:
s1=float(input("Enter game1 score"))
s2=float(input("Enter game2 score"))
s3=float(input("Enter  game3 score"))
s4=float(input("Enter  game4 score"))
s5=float(input("Enter  game3 score"))
list=[s1,s2,s3,s4,s5]
number_score=len(list)
sum=0
for score in list:
    sum=sum+score
    print(sum)
    avg=sum/number_score
    print(avg)
    if (avg>70):
        print("You are qualified for next round")
    else:
        print("Better luck next time")
