# wind chill :

air_temp = float(input('enter the air temperature(in deg celsius):'))
wind_temp = float(input('enter the wind speed(km/h):'))

wind_chillindex = 13.12 + 0.6215 * air_temp - 11.37 *(wind_temp **0.16) + 0.3965 * air_temp *(wind_temp **0.16)

print(wind_chillindex)