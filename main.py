import models


def next_player(currentPlayer, players):
    currentPlayerIndex = players.index(currentPlayer)
    if currentPlayerIndex >= len(players)-1:
        nextPlayer = players[0]
    else:
        nextPlayer = players[currentPlayerIndex+1]

    return nextPlayer


player1 = models.Player()
AIPlayer1 = models.AIPlayer()
AIPlayer2 = models.AIPlayer()
players = [player1, AIPlayer1, AIPlayer2]
presidentGame = models.PresidentGame(players)

endGame = False
currentPlayer = None

for player in players:
    for card in player.hand:
        if card.number == 'D' and card.type == '♥':
            print(player.name + " - Premier joueur")
            currentPlayer = player
            break

print("Début du jeu")
while(not endGame):
    print("Nouveau tour")
    trick = models.Trick()
    trick.lastPlayer = currentPlayer
    currentPlayer.show_hand()
    trick.numberOfCards = input("Nombre de cartes : ")
    endTrick = False
    while(not endTrick):
        print(trick.numberOfCards)
        lastPlayerValue = currentPlayer.play(trick.numberOfCards, trick.lastValueOfCards)

        if lastPlayerValue is not None:
            trick.lastValueOfCards = lastPlayerValue
            trick.lastPlayer = currentPlayer

        currentPlayer.show_hand()

        if next_player(currentPlayer, players) == trick.lastPlayer:
            currentPlayer = trick.lastPlayer
            break
        else:
            currentPlayer = next_player(currentPlayer, players)



#for card in player.hand:
#    print(card.number + "" + card.type)
#
#print("----------------")


#for card1 in AIPlayer1.hand:
#    print(card1.number + "" + card1.type)


#print("----------------")


#for card2 in AIPlayer2.hand:
#    print(card2.number + "" + card2.type)
