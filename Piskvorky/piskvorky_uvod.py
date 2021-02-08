def intro():
    # Tisk uvodni zpravy
    Oddelovac = '=*' * 35
    print(f'''
    {Oddelovac}
    Vítejte ve hře Piškvorky
    Pravidla hry:
    Každý hráč může vložit jednu značku v jednom kole do mřížky 3x3.
    Vítěz bude ten, kdo vloží bez přerušení své tři značky
    * horizontálně
    * vertikálně
    * diagonálně
    {Oddelovac}
''', end='\n')