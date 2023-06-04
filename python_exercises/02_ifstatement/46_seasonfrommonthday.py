#season from month and day:

season = {
    (20, "March"): "Spring",
    (21,'June'): "Summer",
    (22,'September'): "Fall",
    (21,'December') :'Winter'
}

day = input("Enter the day: ")
month = input("Enter the name of the month: ").capitalize()
day = int(day)

if (day, month) in season:
    season_name = season[(day, month)]
    print("The season for", month, day, "is", season_name)
else:
    print("No matching season found.")
