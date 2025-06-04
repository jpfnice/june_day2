
data=[5,6,7,10,-2,-4,11,6,7,9]

# version 1:
    
newdata=[]
for e in data:
    newdata.append(e**3)
    
print(data)
print(newdata)

# version 2:
    
def fct(arg):
    return arg**3

newdata=list(map(fct, data))

print(newdata)


# version 3: "list comprehension"

newdata=[e**3 for e in data]
print(newdata)



