price1=float(input("Enter Amount of a toy car:"))
price2=float(input("Enter Amount of a candy bar:"))
price3=float(input("Enter Amount of a comic book:"))
price4=float(input("Enter Amount of a video game:"))
price5=float(input("Enter Amount of a t-shirt:"))
list=[price1,price2,price3,price4,price5]
sum=0
for total in list:
    sum=sum+total
print(sum)
if(sum>100):
    print(f"{sum-100} is OverBudget")