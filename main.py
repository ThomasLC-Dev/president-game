import models


def next_player(currentPlayer, players):
    currentPlayerIndex = players.index(currentPlayer)
    if currentPlayerIndex >= len(players) - 1:
        nextPlayer = players[0]
    else:
        nextPlayer = players[currentPlayerIndex + 1]

    return nextPlayer


player1 = models.Player()
AIPlayer1 = models.AIPlayer()
AIPlayer2 = models.AIPlayer()
players = [player1, AIPlayer1, AIPlayer2]

endProgram = False
havePresident = False

while not endProgram:
    endGame = False
    currentPlayer = None
    presidentGame = models.PresidentGame(players)


    for player in players:

        if havePresident:
            if player.role == "Président":
                currentPlayer = player
                havePresident = False
                break
        else:
            for card in player.hand:
                if card.number == 'D' and card.type == '♥':
                    print(player.name + " - Premier joueur")
                    currentPlayer = player
                    break

        for player in players:
            player.role == ""

    print("Début du jeu")
    while not endGame:

        print("Nouveau tour")
        trick = models.Trick()
        trick.lastPlayer = currentPlayer
        trick.numberOfCards = currentPlayer.select_number_of_cards()
        endTrick = False

        while not endTrick:
            while len(currentPlayer.hand) == 0:
                currentPlayer = next_player(currentPlayer, players)

            lastPlayerValue = currentPlayer.play(trick.numberOfCards, trick.lastValueOfCards)

            if lastPlayerValue is not None:
                trick.lastValueOfCards = lastPlayerValue
                trick.lastPlayer = currentPlayer
            else:
                print(currentPlayer.name + " a passé son tour !")
                print(trick.lastPlayer.name + " : LAST PLAYER")

            if len(currentPlayer.hand) == 0:
                if havePresident:
                    while len(currentPlayer.hand) == 0:
                        currentPlayer = next_player(currentPlayer, players)
                    currentPlayer.role = "Troufion"
                    print(currentPlayer.name + " devient Troufion !")
                    endTrick = True
                    endGame = True
                    break
                else:
                    currentPlayer.role = "Président"
                    print(currentPlayer.name + " devient Président !")
                    havePresident = True

            if next_player(currentPlayer, players) == trick.lastPlayer or trick.lastValueOfCards == "2" or (next_player(currentPlayer, players).role == "Président" and next_player(next_player(currentPlayer, players), players) == trick.lastPlayer):
                if trick.lastPlayer.role != "Président":
                    currentPlayer = trick.lastPlayer
                endTrick = True
            else:
                currentPlayer = next_player(currentPlayer, players)


    continueToPlay = input("Voulez vous faire une autre partie : ")
    if continueToPlay != "Y":
        endProgram = True

# for card in player.hand:
#    print(card.number + "" + card.type)
#
# print("----------------")


# for card1 in AIPlayer1.hand:
#    print(card1.number + "" + card1.type)


# print("----------------")


# for card2 in AIPlayer2.hand:
#    print(card2.number + "" + card2.type)
