class Point:   # __new__(), __init__() __repr__()

    def __init__(self, valX, valY):
        self.x=valX
        self.y=valY
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x+other.x, self.y+other.y)
        if isinstance(other, int):
            return Point(self.x+other, self.y+other)
        
center=Point(0,0) 
# 1) center=Point.__new__()
# 2) center.__init__(0,0)
# 3) __init__(center, 0, 0)

print(center) # <0,0>
# 1) print(center.__repr__())
print("center.x is", center.x)
print("center.y is", center.y)
center.x=5
center.y=4
print(center) # <5,4>

p2=Point(2,1)
print("p2 is", p2)

p3=center+p2
# 1) p3=center.__add__(p2)

print("p3 is", p3) # <7,5>

p3=p3+10
# 1) p3=p3.__add__(10)

print("p3 is", p3)# <17,15>

d=p2.distance(3)
print(d)

if p2 == p3:
    print("Equal")
else:
    print("Different")





