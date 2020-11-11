def vienadojums(x, a, b):
    """
    Funkcija aprēķina lineāra vienādojuma y = a * x + b vērtību
    pie dotas x vērtības, ja doti koeficienti a un b.
    Vērtības funkcijai tiks dotas secībā x, a, b.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem.

    Argumenti:
        x {int vai float} -- x vērtība
        a {int vai float} -- koeficients a
        b {int vai float} -- koeficients b
    Atgriež:
        int vai float -- y vērtība
    Piemēri:
        vienadojums(1, 1, 1.1) == 2.1
        vienadojums(3, 1, -2) == 1.0
        vienadojums(2.0, 2, -5) == -1.0
    """
