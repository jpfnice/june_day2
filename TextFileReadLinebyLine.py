
csvFile=open("values.csv")

title=csvFile.readline()
print("title: ", title)

total=0
lineNumber=1
for line in csvFile:
    
    # if line == "\n":
    #     continue # switch to the next line
    
    if  line != "\n":  # It means: "If the line is not empty:" 
        numbers=line.split(":")
       
        if len(numbers) == 3: # It means: "If the line is composed of 3 elements:" 
            for ix in range(len(numbers)): # for ix in range(3):
                numbers[ix]=int(numbers[ix])
            
            #total = total + int(numbers[0])
            total = total + numbers[0]
        else:
            print(f"Line {lineNumber} is not composed of 3 numbers!!")
    else:
        print(f"Line {lineNumber} is empty")
        
    lineNumber+=1
        
print("Total is", total)
csvFile.close()
