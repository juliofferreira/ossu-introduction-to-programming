# Use mbox-short.txt as the file name
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

sent = {}
for line in handle:
    if line.startswith("From "):
        line_split = line.split(" ")
        key = line_split[1]
        sent[key] = sent.get(key, 0) + 1

max_value = 0
max_key = ""
for key, value in sent.items():
    if value > max_value:
        max_value = value
        max_key = key
        
print(max_key, max_value)

