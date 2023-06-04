# approximate pi:

i = 1
pi = 1
sign = (-1) **(i+1)
diff = 2 * i
for diff in range(0,16):
    print(diff)
    divisors =diff + (diff +1) * (diff +2)
   
    pi += (sign*(4/divisors))
    print(pi)