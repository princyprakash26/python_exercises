#Birth date to astrological sign:

month = input("Enter the birth month : ")
day = int(input("Enter the birth day: "))

if (month == 'january' and 20 <= day <= 31) or (month == 'february' and 1 <= day <= 18):
    sign = "Aquarius"
elif (month == 'february' and 19 <= day <= 29) or (month == 'march' and 1 <= day <= 20):
    sign = "Pisces"
elif (month == 'march' and 21 <= day <= 31) or (month == 'april' and 1 <= day <= 19):
    sign = "Aries"
elif (month == 'april' and 20 <= day <= 30) or (month == 'may' and 1 <= day <= 20):
    sign = "Taurus"
elif (month == 'may' and 21 <= day <= 31) or (month == 'june' and 1 <= day <= 20):
    sign = "Gemini"
elif (month == 'june' and 21 <= day <= 30) or (month == 'july' and 1 <= day <= 22):
    sign = "Cancer"
elif (month == 'july' and 23 <= day <= 31) or (month == 'august' and 1 <= day <= 22):
    sign = "Leo"
elif (month == 'august' and 23 <= day <= 31) or (month == 'september' and 1 <= day <= 22):
    sign = "Virgo"
elif (month == 'september' and 23 <= day <= 30) or (month == 'october' and 1 <= day <= 22):
    sign = "Libra"
elif (month == 'october' and 23 <= day <= 31) or (month == 'november' and 1 <= day <= 21):
    sign = "Scorpio"
elif (month == 'november' and 22 <= day <= 30) or (month == 'december' and 1 <= day <= 21):
    sign = "Sagittarius"
elif (month == 'december' and 22 <= day <= 31) or (month == 'january' and 1 <= day <= 19):
    sign = "Capricorn"
else:
    sign = "Invalid date"

print("Your astrological sign is:", sign)
