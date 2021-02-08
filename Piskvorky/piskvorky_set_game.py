import random

def set_game():

    # hra má smysl jen při velikosti pole 3x3x a vyšší
    while True:
        # Ziskani velikosti hraci plochy
        size = input('Prosím, vložte velikost hrací plochy (minimálně 3): ')

        # osetreni velikosti a znaku
        if size.isalpha() or int(size) < 3:
            print('Zadali jste chybnou hodnotu. Prosím, zadejte minimálně hodnotu 3 a výše.')
            continue

        else:
            # List pro hraci plochu
            play_area = []

            # Nahrani jednotlivych poli
            for row in range(int(size)):
                play_area.append([' '] * int(size))

            # Zvoleni hrace
            first_play = random.choice(['x', 'o'])
            # Vraceni tuplu hraci plochy a hrace
            return play_area, first_play
            break





