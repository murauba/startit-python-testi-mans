def ir_augoss(saraksts):
    """
    Funkcija akceptē vienu argumentu - masīvu ar skaitļiem 
    un noskaidro vai masīvs ir augošs.
    Masīvs skaitās augošs, ja visi skaitļi masīvā atrodas augošā secībā,
    t.i. katrs skaitlis ir strikti lielāks par iepriekšējo skaitli vai arī
    masīvs ir tukšs vai tajā ir tikai viens elements.
    Ja masīvs ir augošs, atgriež True, pretēja gadījumā atgriež False.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem.

    Argumenti:
        saraksts {list} -- skaitļu saraksts
    Atgriež:
        boolean -- vai skaitļi masīvā ir augošā secībā
    Piemēri:
        ir_augoss([1, 3, 5]) == True
        ir_augoss([100, 10, 180]) == False
        ir_augoss([]) == True
    """
