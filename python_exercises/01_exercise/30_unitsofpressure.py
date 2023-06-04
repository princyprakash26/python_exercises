# units of pressure:

pressure = float(input('enter the pressure in kilopascals:'))
pressure_psi = 0.145038
pressure_mmhg = 7.50062
pressure_atm = 0.00986923

pressure_to_psi = pressure * pressure_psi
pressure_to_mmhg = pressure * pressure_mmhg
pressure_to_atm = pressure * pressure_atm


print(pressure_to_atm)
print(pressure_to_mmhg)
print(pressure_to_psi)