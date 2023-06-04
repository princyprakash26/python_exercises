#taxi fare:

'''
taxi fare= 4.00
for 140 meters=0.25
base fare=0.2
'''
base_fare=2.0
taxi_fare=4.00
for_140_meters=0.25

def distance(km):
    meters=distance*1000
    total=base_fare + (km * taxi_fare) + (meters / 140 * for_140_meters)
    return total


distance_km=float(input('enter the km:'))
fare=distance(distance_km)
print(fare)