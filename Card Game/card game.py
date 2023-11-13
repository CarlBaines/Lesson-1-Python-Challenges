from random import shuffle #imports
from time import sleep
import json

#list of authorised usernames
authorisedPlayers = ['carl123', 'nathan123', 'hazza123']


#menu + authentication
print('-------Welcome to the card game-------')




sleep(.4)
username1 = input('Please enter an authorised username for player one ')


sleep(.4)
username2 = input('Please enter an authorised username for player two ')


while True:

    if username1 in authorisedPlayers:
        break
    else:
        print("Invalid username please try again :(")
        username1 = input('Please enter an authorised username for player one ')



while True:

    if username2 in authorisedPlayers and username2 != username1:
        break
    elif username2 == username1:
        print("The username entered has already been chosen for player one. Please enter a different valid username.")
        username2 = input('Please enter an authorised username for player two ')
    else:
        print("Invalid username please try again :(")
        username2 = input('Please enter an authorised username for player two ')
        



def game():

    #sets both of the player's card counters to 0.
    playerOneCardCounter = 0

    playerTwoCardCounter = 0

    cards = []

    for colour in ["red", "yellow", "black"]:   #loops through the possible colours and adds a colour and number key and value to the 'cards' list. Ten cards are created for each colour.
        for x in range(1,11): 
            cards.append({"colour": colour, "number": x})



    #randomly shuffles the cards.
    shuffle(cards)

    #outputs the cards in a readable format. Use this to check if cards are shuffled appropriately.
    """
    print(json.dumps(cards, indent=3))

    """

    playerOnePickedCard = None
    playerTwoPickedCard = None

    #creates two empty lists for the cards chosen from each player to be stored in. 
    playerOneCards = []

    playerTwoCards = []


    #picks card from the top of the deck for either player one or two - takes the first colour and number values from the list.
    #the loop increments by 2 so that it allows both players to pick a card for each iteration.
    for x in range(0, len(cards), 2):

        playerOnePickedCard = {"colour": cards[x]["colour"], "number": cards[x]["number"]}
        

        if x + 1 < len(cards):
            playerTwoPickedCard = {"colour": cards[x + 1]["colour"], "number": cards[x + 1]["number"]}

        else:
            playerTwoPickedCard = None


        #runs the code if both player one and player two have picked a card.
        if playerOnePickedCard is not None and playerTwoPickedCard is not None:

            if playerOnePickedCard["colour"] == playerTwoPickedCard["colour"]: #scenario for same colour cards.
                if playerOnePickedCard["number"] > playerTwoPickedCard["number"]:
                    sleep(.4)

                    print("\nPlayer One wins!")

                    #adds two cards to the winner's card counter since they win the opponent's card.
                    playerOneCardCounter += 2

                    print("\nNumber of cards (Player One): " + str(playerOneCardCounter))
                    print("Number of cards (Player Two): " + str(playerTwoCardCounter))

                    input('Press enter to play the next round ')

                    sleep(.4)
                    #adds the picked cards of player one and two to the player one cards list.
                    playerOneCards.extend([playerOnePickedCard, playerTwoPickedCard])

                    
                else:
                    sleep(.4)


                    print("\nPlayer Two wins!")

                    playerTwoCardCounter += 2


                    print("\nNumber of cards (Player One): " + str(playerOneCardCounter))
                    print("Number of cards (Player Two): " + str(playerTwoCardCounter))

                    input('Press enter to play the next round ')
                    playerTwoCards.extend([playerTwoPickedCard, playerOnePickedCard])




            else:
                
                #scenarios for different coloured cards.
                if playerOnePickedCard["colour"] == "red":
                    if playerTwoPickedCard["colour"] == "black":
                        sleep(.4)

                        print("\nPlayer One wins!")

                        playerOneCardCounter += 2

                        print("\nNumber of cards (Player One): " + str(playerOneCardCounter))
                        print("Number of cards (Player Two): " + str(playerTwoCardCounter))

                        input('Press enter to play the next round ')
                        playerOneCards.extend([playerOnePickedCard, playerTwoPickedCard])


                    else:
                        sleep(.4)

                        print("\nPlayer Two wins!")

                        playerTwoCardCounter += 2

                        print("\nNumber of cards (Player One): " + str(playerOneCardCounter))
                        print("Number of cards (Player Two): " + str(playerTwoCardCounter))

                        input('Press enter to play the next round ')
                        playerTwoCards.extend([playerTwoPickedCard, playerOnePickedCard])

                elif playerOnePickedCard["colour"] == "yellow":
                    if playerTwoPickedCard["colour"] == "red":
                        sleep(.4)

                        print("\nPlayer One wins!")

                        playerOneCardCounter += 2

                        print("\nNumber of cards (Player One): " + str(playerOneCardCounter))
                        print("Number of cards (Player Two): " + str(playerTwoCardCounter))

                        input('Press enter to play the next round ')
                        playerOneCards.extend([playerOnePickedCard, playerTwoPickedCard])


                    else:
                        sleep(.4)

                        print("\nPlayer Two wins!")

                        playerTwoCardCounter += 2

                        print("\nNumber of cards (Player One): " + str(playerOneCardCounter))
                        print("Number of cards (Player Two): " + str(playerTwoCardCounter))
                        
                        input('Press enter to play the next round ')
                        playerTwoCards.extend([playerTwoPickedCard, playerOnePickedCard])



                elif playerOnePickedCard["colour"] == "black":
                    if playerTwoPickedCard["colour"] == "yellow":
                        sleep(.4)

                        print("\nPlayer One wins!")

                        playerOneCardCounter += 2

                        print("\nNumber of cards (Player One): " + str(playerOneCardCounter))
                        print("Number of cards (Player Two): " + str(playerTwoCardCounter))

                        input('Press enter to play the next round ')
                        playerOneCards.extend([playerOnePickedCard, playerTwoPickedCard])

                                            

                    else:
                        sleep(.4)

                        print("\nPlayer Two wins")

                        playerTwoCardCounter += 2

                        print("\nNumber of cards (Player One): " + str(playerOneCardCounter))
                        print("Number of cards (Player Two): " + str(playerTwoCardCounter))

                        input('Press enter to play the next round ')
                        playerTwoCards.extend([playerTwoPickedCard, playerOnePickedCard])


                    #decides who the winner is and outputs them.

    if playerOneCardCounter > playerTwoCardCounter:
        print("\nGame Over!")
        print('')
        print(username1 + ' is the winner with ' + str(playerOneCardCounter) + ' cards')

        winner = username1
        winning_cards = playerOneCardCounter
        

    elif playerTwoCardCounter > playerOneCardCounter:
        print("\nGame Over!")
        print('')
        print(username2 + ' is the winner with ' + str(playerTwoCardCounter) + ' cards')

        winner = username2
        winning_cards = playerTwoCardCounter
        
    else:
        print("\nGame Over!")
        print('It was a draw!')

        winner = "It's a draw"



    #sets both of the player's picked cards back to their starting values.
    playerOnePickedCard = None
    playerTwoPickedCard = None

    #create a dictionary to store winner information and write to json file.

    winner_info = {"winner": winner, "winning_cards": winning_cards}

    with open("card game leaderboard.json", "a") as file:
        json.dump(winner_info, file, indent = 3)
        file.write("\n")



#plays the game by calling its function and asks the user for a rematch.
while True:
    game()
    playagain = input('Do you want to play again? (y/n) ')
    
    if playagain.lower() != 'y' and playagain.lower() != 'yes':
        break
    else:
        game()






