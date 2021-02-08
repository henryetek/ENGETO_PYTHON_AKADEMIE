import piskvorky_game_over

def board_full(board):
    # Je nejake volne misto v board?
    return ' ' not in piskvorky_game_over.equal(board)


# Funkce pro tisk remízy
def print_tie():
    print('=' * 20)
    print('Nikdo nevyhrák, je to remíza')