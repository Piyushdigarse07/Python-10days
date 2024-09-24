
# di={'s1':{'name':'joe','mark':'68','subject':'maths'},'s2':{'name':'tom','mark':'59','subject':'english'},'s3': {'name':'joe','mark':'63','subject':'science'}}
# print(di)

# to convert string into dictionary and print he dictionary:
s1="name,mark,subject\nJoe,68,maths\nTom,59,english\nAlice,63,science"
data = s1.split("\n")
print(data)

headers= data[0].split(',')
print(headers)

for num,d in enumerate(data[1:],1):
    w=d.split(',')
    d2= dict(zip(headers,w))
    print(num,d2)