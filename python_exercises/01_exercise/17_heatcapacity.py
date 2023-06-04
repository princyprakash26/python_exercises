# heat capacity:

mass_water=float(input('enter the mass of water:'))
temp=float(input('enter the temperature change:'))
heat=4.186
kwh_joule=3600000
energy=mass_water *heat *temp

print(energy)

electricity_rate=8.9
energy_kilowatt=energy/kwh_joule
cost=energy_kilowatt * electricity_rate 