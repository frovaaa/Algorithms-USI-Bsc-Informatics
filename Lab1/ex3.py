def classify_triangle(a,b,c):
    output = ""
    #Set a as max

    # a,b = c,d
    # a becomes c
    # b becomes d

    if b > a and b > c:
        temp = a
        a = b
        b = temp
    elif c > a and c > b:
        temp = a
        a = c
        c = temp

    #print(a,b,c)

    if a <= (b + c) and b <= (a+c) and c <= (a+b):
        #Check angle
        aSq = pow(a,2)
        bSq = pow(b,2)
        cSq = pow(c,2)
        if aSq == (bSq + cSq):
            output += "right "
        elif aSq < (bSq + cSq):
            output += "acute "
        else:
            output += "obtuse "
        
        if (a == b and c > a) or (a == c and b > a) or (c == b and a > c):
            output += "isosceles"
        elif a == b and a == c:
            output += "equilateral"
        else:
            output += "scalene"
    else:
        output += "impossible"

    print(output)

classify_triangle(10,10,10)
classify_triangle(4,3,5)
classify_triangle(4,3,8)
classify_triangle(3,4,3)
classify_triangle(3,5,3)
classify_triangle(5,5,7)

# given three positive numbers representing the lengths of three segments, respectively, 
# output a classification of the triangle obtained by connecting the three segments. 
# The output consists of one or two w
# ords printed on a single line and separated by a single space. 
# The first word is one of acute, right, obtuse, or impossible. impossible indicates that it is 
# impossible to form a triangle with the given segment lengths, in which case the output ends there. 
# Acute, right, and obtuse indicate that the resulting triangle has all acute angles, one right angle, or one obtuse angle. 
# In these cases, the output must contain a second word that can be either scalene, isosceles, or equilateral, indicating the type of triangle.

# trova il lato piu lungo 
# se il quadrato del piu lungo è uguale alla somma dei quadrati degli altri due = il triangolo è rettangolo (ha un angolo retto e due acuti)
# se è minore il triangolo ha solo angoli acuti 
# se è maggiore il triangolo ha un angolo ottuso e due acuti 
# qualunque lato deve essere <= alla somma degli altri due lat

# se due lati sono uguali = isoscele
# se lati sono tutti diversi = scaleno
# se lati sono tutti uguali = equilatero



#Acute < 90
#Right == 90
#Obtuse > 90 and < 180
# Maggiore al quadrato confronto con somma degli atlri 2
# Se piu' piccolo = acuto
# qualunque lato deve essere minore della somma degli altri 2 lati