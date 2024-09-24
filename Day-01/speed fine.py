speed_limit=50
speed= int(input("enter the speed :"))
if(speed<=speed_limit):
    print("Fine:$0")
elif(speed_limit<speed<=speed_limit+10):
    print("Fine:$50")
elif(speed_limit+10<speed<=speed_limit+20):
    print("Fine:$100")
else:
    print("Fine:$200")