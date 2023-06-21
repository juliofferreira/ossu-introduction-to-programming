# Use mbox-short.txt as the file name
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict = {}

for line in handle:
    if line.startswith('From '):
        time = line.split(' ')[6]
        hour = time.split(':')[0]
        dict[hour] = dict.get(hour, 0) + 1

sorted_hours = sorted([(k,v) for k,v in dict.items()])

for k,v in sorted_hours:
    print(f"{k} {v}")