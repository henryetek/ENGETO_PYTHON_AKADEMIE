def game_over(board, player):
    # Velikost hraci plochy
    size = len(board)

    # Prevod na 1D list
    line_board = equal(board)

    # Prochazime kazdou radu
    for i in range(size):

        # Kontrola radku a sloupcu
        if set(line_board[i * size:i * size + size]) == set(player) or set(line_board[i:size ** 2:size]) == set(player):
            return True  # row & column

        # Kontrola diagonaly zleva dolu
        if i == 0 and set(line_board[i:size ** 2:size + 1]) == set(player):
            return True

        # Kontrola diagonaly zprava dolu
        elif i == size - 1 and set(line_board[i:size ** 2 - 1:size - 1]) == set(player):
            return True


# Pomocna funkce pro game_over()
def equal(board):
    eq = []
    # Secti jednotlive radky
    for row in board:
        eq += row
    # vraceni delky radku
    return eq

# Funkce pro tisk vyherce
def print_game_over(player):
    print('='*20)
    print(f'Gratulujeme k vítězství hráči {player}.')