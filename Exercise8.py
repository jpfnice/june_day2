"""
    Define a function addList() which purpose is to add 2 lists
    of numbers given as arguments, element by element.
    
    Example:
        l1=[5,6,3]
        l2=[1,0,-1,10]
        l3=addList(l1, l2) # l3 is [6,6,2,10]
        
"""
d1=[2,3,4,7,8]
d2=[2,23,5]

d3=d1+d2 

d3=addList(d1,d2) 

print(d3) # [4, 26, 9, 7, 8]