
line="23:45:67:89:17:90"

data=line.split(":")

print(data)
# version 1:
    
# for ix in range(len(data)):
#     data[ix]=int(data[ix])
    
# print(data)


# version 2:
    
newdata=list(map(int,data))
print(newdata)