import models


def next_player(current_player, players):
    """
    Function to get the next player
    :param current_player: Current player
    :param players: List of players
    :return: Return the next player
    """
    current_player_index = players.index(current_player)
    if current_player_index >= len(players) - 1:
        next_player = players[0]
    else:
        next_player = players[current_player_index + 1]

    return next_player


player_name = input("Quel est votre nom ?")
player_1 = models.Player(player_name)
AI_player_1 = models.AIPlayer()
AI_player_2 = models.AIPlayer()
players = [player_1, AI_player_1, AI_player_2]

end_program = False
have_president = False

while not end_program:
    end_game = False
    current_player = None
    president_game = models.PresidentGame(players)


    for player in players:

        if have_president:
            if player.role == "Président":
                current_player = player
                have_president = False
                break
        else:
            for card in player.hand:
                if card.number == 'D' and card.type == '♥':
                    print(player.name + " - Premier joueur")
                    current_player = player
                    break

        for player in players:
            player.role == ""

    print("Début du jeu")
    while not end_game:

        print("Nouveau tour")
        trick = models.Trick()
        trick.last_player = current_player
        trick.number_of_cards = current_player.select_number_of_cards()
        end_trick = False

        while not end_trick:
            while len(current_player.hand) == 0:
                current_player = next_player(current_player, players)

            last_player_value = current_player.play(trick.number_of_cards, trick.last_value_of_cards)

            if last_player_value is not None:
                trick.last_value_of_cards = last_player_value
                trick.last_player = current_player
            else:
                print(current_player.name + " a passé son tour !")
                print(trick.last_player.name + " : LAST PLAYER")

            if len(current_player.hand) == 0:
                if have_president:
                    while len(current_player.hand) == 0:
                        current_player = next_player(current_player, players)
                    current_player.role = "Troufion"
                    print(current_player.name + " devient Troufion !")
                    end_trick = True
                    end_game = True
                    break
                else:
                    current_player.role = "Président"
                    print(current_player.name + " devient Président !")
                    have_president = True

            if next_player(current_player, players) == trick.last_player or trick.last_value_of_cards == "2" or (next_player(current_player, players).role == "Président" and next_player(next_player(current_player, players), players) == trick.lastPlayer):
                if trick.last_player.role != "Président":
                    current_player = trick.last_player
                end_trick = True
            else:
                current_player = next_player(current_player, players)


    continue_to_play = input("Voulez vous faire une autre partie : ")
    if continue_to_play != "Y":
        end_program = True
