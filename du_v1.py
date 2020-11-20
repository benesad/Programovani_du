from turtle import forward, left, right, speed, circle, goto, penup, pendown, setpos, exitonclick, dot
from math import *

# PROMENNE --------------------------------------------------


X_body = []
Y_body = []


# PROMENNE --------------------------------------------------


# FUNKCE PRO KONZOLI ----------------------------------------


def writeln(text=""):
    print(text)


def until_right(what, accepted_list):
    value = input(what)
    if value in accepted_list:
        return value
    until_right(what, accepted_list)


def int_check(what):
    try:
        value = input(what)
        num = int(value)
        return num
    except ValueError:
        int_check(what)


def float_or_enter_check(what, check_enter=False):
    try:
        value = input(what)
        if check_enter and value == "":
            return value
        num = float(value)
        return num
    except ValueError:
        int_check(what)


def load_points():
    first = True
    print("Zadejte zeměpisnou šířku a zeměpisnou  délku bodu/ů.")
    while first or input() != 'nope':
        first = False
        print("Zvolte zeměpisnou šířku, je možné celým i desetinným číslem.")
        X_body.append(float_or_enter_check("Zeměpisná šířka: "))
        print("Zvolte zeměpisnou délku, je možné celým i desetinným číslem.")
        Y_body.append(float_or_enter_check("Zeměpisná délka: "))
        print("Je možné přidat další body, chcete možnost využít? Pokud ne, napiště nope.")


# FUNKCE PRO KONZOLI ----------------------------------------


# KRESLICI FUNKCE -------------------------------------------


# MARINA VALCOVE start

"""FUNKCE PRO VÝPOČET MARINOVA VÁLCOVÉHO ZOBRAZENÍ"""

def marina_print_parallel(u, ky):
    for v in range(0, 180, 10):
        if v == 0:
            penup()
        else:
            pendown()
        y = (R * radians(u))
        x = (R * radians(v))
        setpos(x, ky*y)
        setpos(-x, ky*y)


def marina_print(v, kx, ky):
    for u in range(0, 100, 10):
        if u == 0:
            penup()
        else:
            pendown()
        y = (R * radians(u))
        x = (R * radians(v))
        setpos((kx*x), (ky*y))

def marina(R):
    """FUNKCE PRO KRESBU MARINOVA VÁLCOVÉHO ZOBRAZENÍ"""
    for u in range(0, 90, 10):
        marina_print_parallel(u, 1)
    for u in range(0, 90, 10):
        marina_print_parallel(u, -1)
    for v in range(0, 180, 10):
        marina_print(v, 1, 1)
        marina_print(v, -1, 1)
        marina_print(v, 1, -1)
        marina_print(v, -1, -1)

def marina_valcove_body(R):     
    """FUNKCE PRO BODY V KRESBĚ MARINOVA VÁLCOVÉHO ZOBRAZENÍ"""
    for i in range(len(X_body)):
        a = round(R * radians(Y_body[i]), 2)
        b = round(R * radians(X_body[i]), 2)
        print(f"Bod č. {i}: Přepočtená souřadnice zeměpisné šířky je {b} a souřadnice zeměpisné délky {a}.")
        penup() 
        setpos(a,b)
        pendown()
        dot(10)
    exitonclick()

# MARINA VALCOVE end


# zatim neni jasne start 


# zatim neni jasne end


# LAMBERT KUZELOVE start


# LAMBERT KUZELOVE end


# SANSON start

"""FUNKCE PRO VÝPOČET SANSONOVA NEPRAVÉHO ZOBRAZENÍ"""

def sanson_print_parallel(u, ky):
    for v in range(0, 180, 10):
        if v == 0:
            penup()
        else:
            pendown()
        y = (R * radians(u))
        x = (R * radians(v) * cos(radians(u)))
        setpos(x, ky*y)
        setpos(-x, ky*y)


def sanson_print(v, kx, ky):
    for u in range(0, 100, 10):
        if u == 0:
            penup()
        else:
            pendown()
        y = (R * radians(u))
        x = (R * radians(v) * cos(radians(u)))
        setpos((kx*x), (ky*y))


def sanson(R):      
    """FUNKCE PRO KRESBU SANSONOVA NEPRAVÉHO ZOBRAZENÍ"""
    for u in range(0, 90, 10):
        sanson_print_parallel(u, 1)
    for u in range(0, 90, 10):
        sanson_print_parallel(u, -1)
    for v in range(0, 180, 10):
        sanson_print(v, 1, 1)
        sanson_print(v, -1, 1)
        sanson_print(v, 1, -1)
        sanson_print(v, -1, -1)


def sanson_body(R):     
    """FUNKCE PRO BODY V KRESBĚ SANSONOVA NEPRAVÉHO ZOBRAZENÍ"""
    for i in range(len(X_body)):
        a = round(R * radians(Y_body[i]) * cos(radians(X_body[i])), 2)
        b = round(R * radians(Y_body[i]), 2)
        print(f"Bod č. {i}: Přepočtená souřadnice zeměpisné šířky je {b} a souřadnice zeměpisné délky {a}.")
        penup() 
        setpos(a,b)
        pendown()
        dot(10)
    exitonclick()

# SANSON end

# KRESLICI FUNKCE -------------------------------------------


# PRUBEH ----------------------------------------------------


writeln()
writeln("Dobrý den, které zobrazení po mě chcete vypracovat?")
writeln()
writeln("MVZ - MARINOVO VÁLCOVÉ ZOBRAZENÍ")
writeln("xx - zatim neni jasne co")
writeln("LKZ - LAMBERTOVO KUŽELOVÉ ZOBRAZENÍ")
writeln("SNZ - SANSONOVO NEPRAVÉ ZOBRAZENÍ")

# zkratka musi byt v senzamu - check value
value = until_right("Zobrazení: ", ["MVZ", "xx", "LKZ", "SNZ"])

# kontrola polomeru - intiger check
writeln("Zvolte prosím v jakém měřítku byste chtěli vykreslit vybrané zobrazení (1 : 'Vámi zadané číslo')")
scale = int_check("")

# zadany polomer musi byt float - check
writeln("Zvolte poloměr Země, který chcete použít pro výpočet, nebo stiskněte enter pro výpočet s reálným (6371,11 km)")
radius = float_or_enter_check("Poloměr: ", True)
# pri stiknuti enteru díky definici fuknce float_or_enter_check pouzije program realny polomer Zeme
if radius == "":
    radius = 6371.11

load_points()
R = (radius*100000)/scale/0.03
speed(0)

if value == "MVZ":
    marina(R)
    marina_valcove_body(R)
elif value == "xx":
    xx(R)
    xx_b(R)
elif value == "LKZ":
    lambert(R)
    lambertkuz_body(R)
elif value == "SNZ":
    sanson(R)
    sanson_body(R)


# PRUBEH ----------------------------------------------------
