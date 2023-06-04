#chinese zodiac:
'''Rat: 2020, 2008, 1996, 1984, 1972, 1960,
Ox: 2021, 2009, 1997, 1985, 1973, 1961,
Tiger: 2022, 2010, 1998, 1986, 1974, 1962,
Rabbit: 2023, 2011, 1999, 1987, 1975, 1963,
Dragon: 2024, 2012, 2000, 1988, 1976, 1964,
Snake: 2025, 2013, 2001, 1989, 1977, 1965,
Horse: 2026, 2014, 2002, 1990, 1978, 1966,
Goat: 2027, 2015, 2003, 1991, 1979, 1967,
Monkey: 2028, 2016, 2004, 1992, 1980, 1968
Rooster: 2029, 2017, 2005, 1993, 1981, 1969
Dog: 2030, 2018, 2006, 1994, 1982, 1970
Pig: 2031, 2019, 2007, 1995, 1983, 1971'''

year = int(input("enter the year:"))

if year == 2021 or year == 2009 or year == 1997 or year == 1973 or year == 1961 or year == 1985:
    print("Ox")
elif year == 2020 or year == 2008 or year == 1996 or year == 1984 or year == 1972 or year == 1960:
    print("Rat")
elif year == 2023 or year == 2011 or year == 1999 or year == 1975 or year == 1963 or year == 1987:
    print("Rabbit")
elif year == 2024 or year == 2012 or year == 2000 or year == 1988 or year == 1976 or year == 1964:
    print("Dragon")
elif year == 2025 or year == 2013 or year == 2001 or year == 1989 or year == 1977 or year == 1965:
    print("Snake")
elif year == 2026 or year == 2014 or year == 2002 or year == 1990 or year == 1978 or year == 1966:
    print("Horse")
elif year == 2027 or year == 2015 or year == 2003 or year == 1991 or year == 1979 or year == 1967:
    print("Goat")
elif year == 2028 or year == 2016 or year == 2004 or year == 1992 or year == 1980 or year == 1968:
    print("Monkey")
elif year == 2029 or year == 2017 or year == 2005 or year == 1993 or year == 1981 or year == 1969:
    print("Rooster")
elif year == 2030 or year == 2018 or year == 2006 or year == 1994 or year == 1982 or year == 1970:
    print("Dog")
elif year == 2031 or year == 2019 or year == 2007 or year == 1995 or year == 1983 or year == 1971:
    print("Pig")
else:
    print("enter the correct year")
