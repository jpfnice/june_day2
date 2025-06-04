data=[5,6,7,10,-2,-4,11,6,7,9]

# version 1:
    
newdata=[]
for e in data:
    if e%2 == 0:
        newdata.append(e)
    
print(data)
print(newdata)

# version 2:
    
def isEven(arg):
    return arg%2 == 0

newdata=list(filter(isEven, data))

print(newdata)

