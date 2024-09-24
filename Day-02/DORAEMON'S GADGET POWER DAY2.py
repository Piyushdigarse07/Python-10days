anywhereDoor=int(input("enter the power"))

bambooCopter=int(input("enter the power")) 

timeCloth=int(input("enter the power"))

memoryBread=int(input("enter the power"))

translatorJelly=int(input("enter the power"))

totalpower=0

for power in [anywhereDoor,bambooCopter,timeCloth,memoryBread,translatorJelly]:

    totalpower=totalpower+power

    print(totalpower)

if totalpower>=500:

     print("total power is enough to save Nobita from the evil robot")

else:

    print(f"{500-totalpower}how much more power is needed")

