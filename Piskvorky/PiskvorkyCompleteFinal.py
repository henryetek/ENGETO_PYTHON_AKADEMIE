# pod názvem Tic Tac Toe je skrývají české piškvorky
import piskvorky_uvod
import piskvorky_set_game
import piskvorky_play_area
import piskvorky_first_player
import piskvorky_game_over
import piskvorky_tie
import piskvorky_second_player

#výpis návodu
piskvorky_uvod.intro()

# nastavení plochy a výběr hráče, který začíná
board_play, first_player = piskvorky_set_game.set_game()

while True:
    # vykreslení hrací plochy
    piskvorky_play_area.play_area(board_play)

    # táhnutí hráčem
    board_play = piskvorky_first_player.first_player(first_player, board_play)

    # Kontrola výhry
    if piskvorky_game_over.game_over(board_play, first_player):
        # Oznameni o vyhre
        piskvorky_game_over.print_game_over(first_player)
        break

    # Kontrola remízy
    elif piskvorky_tie.board_full(board_play):
        piskvorky_tie.print_tie()
        break

    # vymena hracu
    first_player = piskvorky_second_player.change_players(first_player)

# Tisk vitezne hraci plochy
piskvorky_play_area.play_area(board_play)


