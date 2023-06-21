# Use mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
line_count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line_count = line_count + 1
    colon_position = line.find(":")
    number = float(line[colon_position + 1:].strip())
    total = total + number
    
print("Average spam confidence:", total / line_count)