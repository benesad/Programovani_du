from turtle import forward, left, right, speed, circle, goto, penup, pendown, setpos, exitonclick, dot
from math import *


# -------------------- FUNKCE PRO KONZOLI ----------------------------------------


def until_right(what, accepted_list):
    """Zde dochází k ověření, zda je zadaný vstup validní ze seznamu"""
    while True:
        value = input(what)
        if value in accepted_list:
            return value
        print("Zadaná položka není validní!")


def int_check(what):
    """Zde je kontrolováno, zda je zadaná hodnota integer v případě, že musí"""
    while True:
        try:
            num = int(input(what))
            return num
        except ValueError:
            print("Napište celočíselnou hodnotu!")


def float_check(what):
    """Zde dochází ke kontrole, zda je zadaný vstup číslo"""
    while True:
        try:
            num = float(input(what))
            return num
        except ValueError:
            print("Napište číselnou hodnotu!")


def load_points():
    first = True
    x_points = []
    y_points = []
    print("Zadejte zeměpisnou šířku a zeměpisnou délku bodu/ů které chcete spočítat a vykreslit.")
    while first or input() != '0':
        first = False
        print("Zvolte zeměpisnou šířku, je možné celým i desetinným číslem.")
        x_points.append(float_check("Zeměpisná šířka: "))
        print("Zvolte zeměpisnou délku, je možné celým i desetinným číslem.")
        y_points.append(float_check("Zeměpisná délka: "))
        print("Je možné přidat další body, chcete možnost využít? Pokud ne, napiště 0.")
    return [x_points, y_points]


# ------------------- FUNKCE PRO KONZOLI end ----------------------------------------


# ------------------- KRESLICI FUNKCE -------------------------------------------


# MARINA VALCOVE start

"""Funkce pro výpočet Marinova zobrazení"""

def marina_draw_parralel(u, ky):
    """Funkce pro kresbu poledníků v zobrazení"""
    for v in range(0, 180, 10):
        if v == 0:
            penup()
        else:
            pendown()
        y = (R * radians(u))
        x = (R * radians(v))
        setpos(x, ky*y)
        setpos(-x, ky*y)


def marina_draw_meridian(v, kx, ky):
    """Funkce pro kresbu rovnoběžek v zobrazení"""
    for u in range(0, 100, 10):
        if u == 0:
            penup()
        else:
            pendown()
        y = (R * radians(u))
        x = (R * radians(v))
        setpos((kx*x), (ky*y))

def marina(R):
    """Funkce pro kresbu Marinova válcového zobrazení"""
    for u in range(0, 90, 10):
        marina_draw_parralel(u, 1)
    for u in range(0, 90, 10):
        marina_draw_parralel(u, -1)
    for v in range(0, 180, 10):
        marina_draw_meridian(v, 1, 1)
        marina_draw_meridian(v, -1, 1)
        marina_draw_meridian(v, 1, -1)
        marina_draw_meridian(v, -1, -1)

def marina_points(R, x_points, y_points):
    """Funkce pro body v kresbě Marinova válcového zobrazení + výpočet souřadnic zadaných uživatelem."""
    for i in range(len(x_points)):
        a = round(R * radians(y_points[i]), 2)
        b = round(R * radians(y_points[i]), 2)
        print(f"Bod č. {i}: Přepočtená souřadnice zeměpisné šířky je {b} a souřadnice zeměpisné délky {a}.")
        """Následující řádky zakreslí body (a,b) do nakreslého zobrazení"""
        penup() 
        setpos(a,b)
        pendown()
        dot(10)
    exitonclick()

# MARINA VALCOVE end ----------------------------------


# ORTOGRAPHIC start ----------------------------------

def ortographic_draw_parallel(v, ky):
    """Funkce pro kresbu poledníků v zobrazení"""
    for u in range(1, 38):
        left(10)
        forward(R * sin(radians(180)))
        goto(0,0)
        penup()
        left(90)
        forward(R * sin(radians((16 * 5))))
        left(90)
        pendown()

def ortographic_draw_meridian(u, kx, ky):
    """Funkce pro kresbu poledníků v zobrazení"""
    for v in range(19, 0, -1):
        circle(R * sin(radians((v * 5))))
        right(90)
        penup()
        forward((R * sin(radians((v * 5)))) - (R * sin(radians(((v + 1) * 5)))))
        pendown()
        left(90)

    
def ortographic_az(R):
    """Funkce pro kresbu Ortografického zobrazení"""
    for u in range(1, 11, 10):
        ortographic_draw_parallel(u, 1)
    for v in range(1, 180, 180):
        ortographic_draw_meridian(v, 1, 1)


def ortographic_points(R, x_points, y_points):
    """Funkce pro body v kresbě Ortografického zobrazení + výpočet souřadnic zadaných uživatelem."""
    for i in range(len(x_points)):
        a = round(R * sin(radians(x_points[i])), 2)
        b = round(R * (sin(radians((y_points[i] * 5)))) - sin(radians(((y_points[i] + 1) * 5))), 2)
        print(f"Bod č. {i}: Přepočtená souřadnice zeměpisné šířky je {b} a souřadnice zeměpisné délky {a}.")
        """Následující řádky zakreslí body (a,b) do nakreslého zobrazení"""
        penup() 
        setpos(a,b)
        pendown()
        dot(10)
    exitonclick()

# ORTOGRAPHIC end --------------------------


# LAMBERT KUZELOVE start -------------------

u = (36 * (10 * (cos(15) ** 2)) - 180) / 2

def lambertkuz_draw_parallel(u, ky):
    """Funkce pro kresbu poledníků v zobrazení"""
    for v in range(1, 19):
        if v == 0:
            penup()
        else:
            pendown()
        y = (2 * R * (sin(radians((45))))) / ((cos(pi/2 - radians(pi/6)))/2)
        x = (10 * radians(cos(pi/2-pi/6)/2) ** 2)
        circle(-2 * R * (sin(radians((v * 5))) / cos(radians(15))), 180 + u + u)
        setpos(x, ky*y)
        setpos(-x, ky*y)

def lambertkuz_draw_meridian(v, kx, ky):
    """Funkce pro kresbu poledníků v zobrazení"""
    for i in range(1, 37):
        if i == 0:
            penup()
        else:
            pendown()
        y = (2 * R * (sin(radians((45))))) / ((cos(pi/2 - radians(pi/6)))/2)
        x = (10 * radians(cos(pi/2-pi/6)/2) ** 2)
        circle(-2 * R * (sin(radians((v * 5))) / cos(radians(15))), 180 + u + u)
        setpos((kx*x), (ky*y))

def lambert(R):    
    """Funkce pro kresbu Lambertova kuželového zobrazení"""
    for u in range(0, 90, 10):
        lambertkuz_draw_parallel(u, 1)
    for u in range(0, 90, 10):
        lambertkuz_draw_parallel(u, -1)
    for v in range(1, 19):
        lambertkuz_draw_meridian(v, 1, 1)
        lambertkuz_draw_meridian(v, -1, 1)


def lambertkuz_points(R):   
    """Funkce pro body v kresbě Lambertova kuželového zobrazení + výpočet souřadnic zadaných uživatelem."""
    for i in range(len(x_points)):
        a = round(10 * cos(15) ** 2 * (y_points[i]), 2)
        b = round(2 * R * sin(radians(y_points[i])) / cos(radians(x_points[i])), 2)
        print(f"Bod č. {i}: Přepočtená souřadnice zeměpisné šířky je {b} a souřadnice zeměpisné délky {a}.")
        penup() 
        setpos(a,b)
        pendown()
        dot(10)
    exitonclick()

# LAMBERT KUZELOVE end ----------------


# SANSON start -----------------------------

"""Funkce pro výpočet Sansonova nepravého zobrazení"""

def sanson_draw_parallel(u, ky):
    """Funkce pro kresbu poledníků v zobrazení"""
    for v in range(0, 180, 10):
        if v == 0:
            penup()
        else:
            pendown()
        y = (R * radians(u))
        x = (R * radians(v) * cos(radians(u)))
        setpos(x, ky*y)
        setpos(-x, ky*y)


def sanson_draw_meridian(v, kx, ky):
    """Funkce pro kresbu rovnoběžek v zobrazení"""
    for u in range(0, 100, 10):
        if u == 0:
            penup()
        else:
            pendown()
        y = (R * radians(u))
        x = (R * radians(v) * cos(radians(u)))
        setpos((kx*x), (ky*y))


def sanson(R):      
    """Funkce pro kresbu Sansonova nepravého zobrazení"""
    for u in range(0, 90, 10):
        sanson_draw_parallel(u, 1)
        sanson_draw_parallel(u, -1)
    for v in range(0, 180, 10):
        sanson_draw_meridian(v, 1, 1)
        sanson_draw_meridian(v, -1, 1)
        sanson_draw_meridian(v, 1, -1)
        sanson_draw_meridian(v, -1, -1)


def sanson_points(R, x_points, y_points):
    """Funkce pro body v kresbě Sansonova nepravého zobrazení + výpočet souřadnic zadaných uživatelem."""
    for i in range(len(x_points)):
        a = round(R * radians(y_points[i]) * cos(radians(x_points[i])), 2)
        b = round(R * radians(y_points[i]), 2)
        print(f"Bod č. {i}: Přepočtená souřadnice zeměpisné šířky je {b} a souřadnice zeměpisné délky {a}.")
        """Následující řádky zakreslí body (a,b) do nakreslého zobrazení"""
        penup() 
        setpos(a,b)
        pendown()
        dot(10)
    exitonclick()

# SANSON end -----------------------

# ------------------ KRESLICI FUNKCE end -------------------------------------------


# ------------------ PRUBEH start ----------------------------------------------------



print("Dobrý den, které zobrazení po mně chcete vypracovat?")
print()
print("Ma - Marinovo zobrazení")
print("Or - Ortografické zobrazení")
print("Lk - Lambertovo zobrazení kuželové - NEFUNGUJE")
print("Sa - Sansonovo zobrazení")

# zkratka musi byt v senzamu - check value
value = until_right("Zobrazení: ", ["Ma", "Or", "Lk", "Sa"])

# kontrola polomeru - intiger check
print("Zvolte prosím v jakém měřítku byste chtěli vykreslit vybrané zobrazení (1 : 'Vámi zadané číslo')")
scale = int_check("")

# zadany polomer musi byt float - check
print("Zvolte poloměr Země, který chcete použít pro výpočet, nebo stiskněte 0 pro výpočet s reálným (6371,11 km)")
radius = float_check("Poloměr: ")
# pri stiknuti 0 díky definici fuknce float_check pouzije program realny polomer Zeme
if radius == 0:
    radius = 6371.11

[x_points, y_points] = load_points()
R = (radius*100000)/scale/0.03
speed(0)

if value == "Ma":
    marina(R)
    marina_points(R, x_points, y_points)
elif value == "Or":
    ortographic_az(R)
    ortographic_points(R, x_points, y_points)
elif value == "Lk":
    lambert(R)
    lambertkuz_points(R)
elif value == "Sa":
    sanson(R)
    sanson_points(R, x_points, y_points)

# ---------------- PRUBEH end ----------------------------------------------------
