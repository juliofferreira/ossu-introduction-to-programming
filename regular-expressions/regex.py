import re

#Use data.txt as the file
name = input("Enter file: ")
handle = open(name)
data_text = handle.read()

numbers_string = re.findall("[0-9]+", data_text)
numbers_int = [int(x) for x in numbers_string]

print(sum(numbers_int))
    