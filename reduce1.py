import functools

data=[5,6,7,10,-2,-4,11,6,7,9]

# version 1:
    
total=0
for e in data:
   total += e
    
print(data)
print(total)

# version 2:
    
def fct(a, b):
    return a+b

total=functools.reduce(fct, data)

print(total)

