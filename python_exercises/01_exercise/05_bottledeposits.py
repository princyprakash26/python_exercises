a = float(input("Enter the number of the bottle size in 1 ltr or below to refund:"))
b = float(input("Enter the number of the bottle size in 1 or above to refund:"))

less = a * 0.10
more = b * 0.25

refund = less+more

print(refund)