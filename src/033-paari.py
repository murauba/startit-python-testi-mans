def skaitlu_vardnica(virkne):
    """
    Funkcija akceptē vienu argumentu - simbolu virkni ar vārdiem,
    un pārvērš to vārdnīcā, katru nepāra vārdu izmantojot kā atslēgu
    un katru pāra vārdu kā atslēgas vērtību.
    Var pieņemt, ka ievades simbolu virknē vienmēr būs vismaz 2 vārdi
    un vārdu skaits vienmēr būs pāra skaitlis.
    Funkcija atgriež izveidoto vārdnīcu.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem.

    Argumenti:
        virkne {string} -- simbolu virkne, vārdi atdalīti ar atstarpi
    Atgriež:
        dictionary -- nepāra vārdi kā atslēgas un pāra kā vērtības
    Piemēri:
        skaitlu_vardnica("viens one") == {'viens': 'one'}
        skaitlu_vardnica("viens one divi two") == {'viens': 'one', 'divi': 'two'}
    """
    vardi = virkne.split()
    vardnica = {}
    for i in range(0, len(vardi), 2):
        vardnica[vardi[i]] = vardi[i+1]
    return vardnica
