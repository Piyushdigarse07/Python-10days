#operators
num1= int(input("enter number 1:"))
num2= int(input("enter number 2:"))
print(num1+num2)
print(num1**num2)

#assignment operators
num1+=10
print(num1)
print(num1==num2)

#logical operator
print((num1>num2) and (num1>10))
print(not(num1<num2))

#comparison operators
print(num1>=num2)
print(num1<=num2)

if num1%2==0:
    print("The number is even")
else:
    print("Number is odd")
