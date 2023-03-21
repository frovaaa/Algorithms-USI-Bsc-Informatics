def median_value(a,b,c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    elif a > c:
        return a
    elif b < c:
        return b
    else:
        return c

print(median_value(1,2,3))
print(median_value(3,2,1))
print(median_value(7,3,21))
print(median_value(7,3,5))
print(median_value(7,3,3))
print(median_value(7,3,7))
