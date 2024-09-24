Year1=int(input("Enter Year1:"))
Year2=int(input("Enter Year2:"))
Year3=int(input("Enter Year3:"))
Year4=int(input("Enter Year4:"))
Year5=int(input("Enter Year5:"))
list=[Year1,Year2,Year3,Year4,Year5]
for year in list:
    print(year)
    if(year==2024):
        print("Present")
    elif(year>2024):
        print("Future")
    else:
        print("Past")