
csvFile=open("values.csv")

title=csvFile.readline()
print("title: ", title)

total=0

for line in csvFile:
    numbers=line.split(":")
    print(numbers)
    
    for ix in range(len(numbers)): # for ix in range(3):
        numbers[ix]=int(numbers[ix])
        
    print(numbers)
    
    #total = total + int(numbers[0])
    total = total + numbers[0]

print("Total is", total)
csvFile.close()
