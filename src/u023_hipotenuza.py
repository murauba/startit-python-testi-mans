import math

def hipotenuza(a, b):
    """
    Funkcija akceptē divus argumentus - katešu garumus un atgriež 
    hipotenūzas garumu, vai 0, ja kaut vienas katetes garums ir <= 0
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem.

    Argumenti:
        a {int vai float} -- katetes a garums
        b {int vai float} -- katetes b garums
    Atgriež:
        int vai float -- hipotenūzas garums
    Piemēri:
        hipotenuza(3, 4) == 5.0
        hipotenuza(3, 0) == 0
    """
    if a > 0 and b > 0:
        rezultats = math.sqrt(a**2 + b**2)
    else:
        rezultats = 0
    return rezultats

# Japārbauda visas argumentu variācijas
# pareizas katetes
print("a=3, b=4, jābūt 5,", hipotenuza(3, 4))
# negatīva katete a
print("a=-3, b=4, jābūt 0, ir", hipotenuza(-3, 4))
# negatīva katete b
print("a=3, b=-4, jābūt 0, ir", hipotenuza(3, -4))
# katete a ir 0
print("a=0, b=3, jābūt 0, ir", hipotenuza(0, 3))
# katete b ir 0
print("a=3, b=0, jābūt 0, ir", hipotenuza(3, 0))
# abas katetes ir 0
print("a=0, b=0, jābūt 0, ir", hipotenuza(0, 0))
# abas katetes ir negatīvas
print("a=-3, b=-4, jābūt 0, ir", hipotenuza(-3, -4))
