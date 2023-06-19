hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate Per Hour:")
r = float(rate)

pay = 0
if(h <= 40):
    pay = h * r
else:
    pay = (h - 40) * r * 1.5 + 40 * r
    

print(pay)