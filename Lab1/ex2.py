def leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False

print(leap_year(2000)) #True
print(leap_year(1969)) #False
print(leap_year(2023)) #False
print(leap_year(1984)) #True
print(leap_year(2022)) #False
print(leap_year(2200)) #False
print(leap_year(2400)) #True
print(leap_year(1900)) #False