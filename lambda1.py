import functools

data=[5,6,7,10,-2,-4,11,6,7,9]
    
# def fct(arg):
#     return arg**3
# <=> 
# lambda arg: arg**3

newdata=list(map(lambda arg: arg**3, data))
print(newdata)

# def isEven(arg):
#     return arg%2 == 0

isEven=lambda arg: arg%2==0

newdata=list(filter(isEven, data))
print(newdata)

newdata=list(map(isEven, data))

print(newdata)

# def fct(a, b):
#     return a+b

total=functools.reduce(lambda a,b:a+b, data)

print(total)