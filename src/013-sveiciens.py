""" 
Uzrakstiet programmu, kas ielasa vienu vārdu 
un izvada uz ekrāna sveicienu sekojošā formātā:
"Labrīt, vards!"
Piemēram, ja ievadīts ir vārds "Māris", tad tiek izvadīts:
"Labrīt, Māris!"
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
vards = input("Ievadiet vārdu: ")
print("Labrīt, {}!".format(vards))
