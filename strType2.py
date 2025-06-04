"""
str (string) is a kind of sequence
str is an immutable iterable type

It means you can use:
    len(), for, [index], [ix1:ix2], in, not in, +, *, ...

"""
# Creation of str with the help of formated strings

import math
nb=5
text=f"Nb is {nb}"
print(text)

text=f"Nb is {nb} Nb**3 is {nb**3}"
print(text)

text=f"SQRT of Nb is {math.sqrt(nb)} "
print(text)

text=f"SQRT of Nb is {math.sqrt(nb):.2f} "
print(text)


for ix in [34,56,67]:
    print(ix)
    
for i in range(1,20): # i -> [1,20[
    print(f"{i:<3} -> {math.sqrt(i):.3f}")

print("*"*30)

i=1
while i < 20: 
    print(f"{i:<3} -> {math.sqrt(i):.3f}")
    i+=1
    
    
# data=[3,4,5,6,7,8,9,10]
# print(data)
# data=(list(range(3,11))) # [3,10]
# print(data)
# data=(list(range(3,11,2))) # [3, 5, 7, 9]
# print(data)
# data=(set(range(100))) # [0,99]
# print(data)
