def computepay():
    if h<= 40:
        p = h * r
    elif h>= 40:
        p = (h - 40) * (r * 1.5) + (40 * r)
    return p

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate of pay:")
r = float(rate)
        
print computepay()
