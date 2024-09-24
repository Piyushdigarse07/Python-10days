totalproblems=50
probssolved=int(input('enter how many problems nobita solves each day')) #5
problemsleft=totalproblems #50
 
while(problemsleft>0):
    problemsleft=problemsleft-probssolved #left=50-5
    print('problems solved are:',problemsleft)
    if(probssolved==25):
        print('congratulations nobitha, you have completed half of your problems')
    else:
        print('')
 
 
print(type(probssolved))
