def computepay(h, r):
    if (h <= 40):
        return h * r
    else:
        return (h - 40) * r * 1.5 + 40 * r

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate Per Hour:"))


p = computepay(hrs, rate)
print("Pay", p)