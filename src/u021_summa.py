def summa(a, b):
    """
    Funkcija akceptē divus argumentus - skaiļus a un b,
    aprēķina to summu un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem.

    Argumenti:
        a {int vai float} -- pirmais skaitlis
        b {int vai float} -- otrais skaitlis
    Atgriež:
        int vai float -- argumentu summa
    Piemēri:
        summa(1, 1) == 2
        summa(1.0, -1) == 0.0
        summa(2.5, 1.2) == 3.7
    """
    rezultats = a + b
    return rezultats

# Dažādi veidi kā pārbaudīt
# Nav skaidrs, vai rezultāts ir pareizs, jo nav nekādas papildus informācijas:
print(summa(1, 5.2))
# Tiek izdrukāta informācija par argumentiem, jārēķina un jāsalīdzina "uz aci"
print("1.2 + 3 =", summa(1.2, 3))
# Tiek izdrukāta informācija par sagaidāmo rezultātu, jāsalīdzina "uz aci"
print("Jābūt 2: ", summa(1, 1)) 
# Tiek veikts un izdrukāts salīdzinājums bez papildus info
print(summa(1.2, 2) == 3.2)
# Tiek veikts un izdrukāts salīdzinājums ar papildus info
print("Pārbaude ar argumentiem 1 un 2:", summa(1, 2) == 3)
