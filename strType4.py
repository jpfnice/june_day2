"""
str (string) is a kind of sequence
str is an immutable iterable type

It means you can use:
    len(), for, [index], [ix1:ix2], in, not in, +, *, ...

"""
# Methods available:

text="value1:value2:value3:value4"
result=text.split(":")
print(result)

text="123:345:356:789"
result=text.split(":")
print(result)

text="value1   value2 value3      value4"
result=text.split()
print(result)

data=['12', '234', '789', '89']
result=";".join(data)
print(result)

name="mArCO"
m1=name.capitalize()
print(name, m1)
m1=name.upper()
print(name, m1)
m1=name.lower()
print(name, m1)

file="data_name_1234_567.txt"
print(file)
file=file.replace("_", "")
print(file)

data="file1.txt"

if data.endswith("pdf"):
    print(f"{data} is a PDF document")
else:
    print(f"{data} does not have the pdf extension")
    
data="***234***"
data2=data.strip("*")
print(data2)
number=int(data2)
print(number)
print("data is", data)
print("data.rstrip('*')", data.rstrip("*"))
print("data.lstrip('*')", data.lstrip("*"))
print("data.strip('*')", data.strip("*"))
print("data2 is", data2)

print("length of data is:", len(data))

print("data[2:5]", data[2:5])





