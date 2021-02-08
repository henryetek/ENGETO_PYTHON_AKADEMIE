def play_area(board):
    # List pro tisk hraci plochy
    desk = []

    # Velikost hraci plochy
    size = len(board)
    print(size)

    # Nahrati vrchniho ohraniceni hraci plochy do b
    desk.append('\n' + '-' * size * 2 + '\n')

    # Pro kazdy radek
    for row in board:
        # Nahrej cleny radku do b, spoj je znakem '|' a zakonci novym radkem
        desk.append('|'.join(row) + '\n')
        # Nahrej size-krat znak '-' do b a zakonci novym radkem
        desk.append('-' * size * 2 + '\n')

        # Vytiskni jako string vsechny cleny b

    print(''.join(desk))


