#ideal gas law:

Pressure = float(input('enter the value of pressure:'))
volume = float(input('enter the value of volume:'))
temp_cel = float(input('enter temperature in (celsius):'))

R = 8.314
temp_kel = temp_cel+273.15
moles = (Pressure * volume)/(R*temp_kel)

print(moles)
