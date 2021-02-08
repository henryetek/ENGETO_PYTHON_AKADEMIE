def first_player(player, board):
    while True:

        # Vyzva k tahu
        input_first_player = input(f'Hráč {player} | Prosím vlož číslo pole:')

        #kontrola vstupu
        if input_first_player.isalpha() or int(input_first_player) == 0 or int(input_first_player) > (len(board) **2):
            print('zadana hodnota je mimo rozsah!')
            continue
            # souradnice zadane pozice
        else:
            row, col = point_board(int(input_first_player), len(board))

            # Pokud je pole prazdne
            if board[row][col] == ' ':
                # Vloz symbol hrace
                board[row][col] = player
                break

            # Pokud je pole obsazeno
            else:
                print('\nPozice je obsazena.\n')
                continue

    # vracení plochy
    return board


# Získání souřadnic
def point_board(first_play_pos, size):
    # Ziskani souradnice slopce ze skalaru
    column = (first_play_pos - 1) % size

    # Ziskani souradnice radku ze skalaru
    row_b = round((first_play_pos - column) // size)

    # Vracenime radek a sloupec
    return row_b, column
