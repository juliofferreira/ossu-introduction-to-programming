text = "X-DSPAM-Confidence:    0.8475"

colon_position = text.find(":")

string_number = text[colon_position + 1:].lstrip()

print(float(string_number))