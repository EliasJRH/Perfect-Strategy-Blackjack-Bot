import random
import blackjackPerfectAI
import blackjackOnlyCountAI
import blackjackOnlyDecisionsAI
import simplebot 
import os
#Importing all the bots


full_deck = [] # lists to hold the full deck and player hands


# The goal of blackjack.py is to simulate a normal game of blackjack
# Therefore, everything happening on this file will not be related to card counting
# or blackjack basic strategy. Everytime that a function from blackjackPerfectAI is used
# either some form of card counting or blackjack basic strategy is being applied
def initgame(): # initializes the game
    # The way that the statistics in the game will be calculated are in sets
    # A set consists of 100 rounds of the game, a set is considered to be won
    # if the amount of cash the AI has at the end is greater than the amount of cash they started with
    # At the end that amount of sets that were won as well as the win percentage are displayed
    
    #Creates all the statistics for each bot
    sets_won_perfect = 0
    highest_amnt_perfect = None
    lowest_amnt_perfect = None
    average_perfect = 0
    
    sets_won_onlycount = 0
    highest_amnt_onlycount = None
    lowest_amnt_onlycount = None
    average_onlycount = 0
    
    sets_won_onlydecisions = 0
    highest_amnt_onlydecisions = None
    lowest_amnt_onlydecisions = None
    average_onlydecisions = 0
    
    sets_won_simplebot = 0
    highest_amnt_simplebot = None
    lowest_amnt_simplebot = None
    average_simplebot = 0
    
    sets = 200
    reshuffle() # starts the game with a fresh deck
    
    #O(n) operation, first for loop runs for a changeable number of sets,
    #second for loop always runs 100 times
        
    for y in range(sets):
    
        for x in range(100):
            startgame() # starts a single round of the game
        if blackjackPerfectAI.cash >= blackjackPerfectAI.starting_cash: 
            # At the end of the set, the amount of cash that AI has it checked to see if it won or lost
            sets_won_perfect += 1
        #Then the amount of cash is checked to see if it's the greatest the bot has won or the lowest
        if highest_amnt_perfect == None or blackjackPerfectAI.cash > highest_amnt_perfect:
            highest_amnt_perfect = blackjackPerfectAI.cash
        if lowest_amnt_perfect == None or blackjackPerfectAI.cash < lowest_amnt_perfect:
            lowest_amnt_perfect = blackjackPerfectAI.cash
        #Finally, the amount they won is added to an average that will be calculated when all the sets finish
        average_perfect += blackjackPerfectAI.cash   
            
        #This process is repeated for the other bots that only use one of the two strategies
        if blackjackOnlyCountAI.cash >= blackjackOnlyCountAI.starting_cash:
            sets_won_onlycount += 1
        if highest_amnt_onlycount == None or blackjackOnlyCountAI.cash > highest_amnt_onlycount:
            highest_amnt_onlycount = blackjackOnlyCountAI.cash
        if lowest_amnt_onlycount == None or blackjackOnlyCountAI.cash < lowest_amnt_onlycount:
            lowest_amnt_onlycount = blackjackOnlyCountAI.cash
        average_onlycount += blackjackOnlyCountAI.cash
         
        if blackjackOnlyDecisionsAI.cash >= blackjackOnlyDecisionsAI.starting_cash:
            sets_won_onlydecisions += 1
        if highest_amnt_onlydecisions == None or blackjackOnlyDecisionsAI.cash > highest_amnt_onlydecisions:
            highest_amnt_onlydecisions = blackjackOnlyDecisionsAI.cash
        if lowest_amnt_onlydecisions == None or blackjackOnlyDecisionsAI.cash < lowest_amnt_onlydecisions:
            lowest_amnt_onlydecisions = blackjackOnlyDecisionsAI.cash
        average_onlydecisions += blackjackOnlyDecisionsAI.cash
        
        if simplebot.cash >= simplebot.starting_cash:
            sets_won_simplebot += 1
        if highest_amnt_simplebot == None or simplebot.cash > highest_amnt_simplebot:
            highest_amnt_simplebot = simplebot.cash
        if lowest_amnt_simplebot == None or simplebot.cash < lowest_amnt_simplebot:
            lowest_amnt_simplebot = simplebot.cash
        average_simplebot += simplebot.cash
        
        reset_ai()
        reshuffle()
        print('SET DONE')
        
    print(f'Sets played: {sets}')
    print('Stats:')
    print(f'Player 1 (Perfect strategy + Card counting): \n  Sets won: {sets_won_perfect} \n  Set win percentage: {(sets_won_perfect / sets) * 100} \n  Average payout: {average_perfect / sets} \n  Best payout: {highest_amnt_perfect} \n  Worst loss: {lowest_amnt_perfect}')
    print(f'Player 2 (Only card counting): \n  Sets won: {sets_won_onlycount} \n  Set win percentage: {(sets_won_onlycount / sets) * 100} \n  Average payout: {average_onlycount / sets} \n  Best payout: {highest_amnt_onlycount} \n  Worst loss: {lowest_amnt_onlycount}')
    print(f'Player 3 (Only perfect strategy): \n  Sets won: {sets_won_onlydecisions} \n  Set win percentage: {(sets_won_onlydecisions / sets) * 100} \n  Average payout: {average_onlydecisions / sets} \n  Best payout: {highest_amnt_onlydecisions} \n  Worst loss: {lowest_amnt_onlydecisions}')
    print(f'Player 4 (No strategies used): \n  Sets won: {sets_won_simplebot} \n  Set win percentage: {(sets_won_simplebot / sets) * 100} \n  Average payout: {average_simplebot / sets} \n  Best payout: {highest_amnt_simplebot} \n  Worst loss: {lowest_amnt_simplebot}')
    
    #Prints all the results to a file
    with open('game_results.txt', 'a+') as game_results:
        game_results.write('/////////////////////------------------\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n')
        game_results.write(f'Player 1 (Perfect strategy + Card counting): \n  Sets won: {sets_won_perfect} \n  Set win percentage: {(sets_won_perfect / sets) * 100} \n  Average payout: {average_perfect / sets} \n  Best payout: {highest_amnt_perfect} \n  Worst loss: {lowest_amnt_perfect}\n  Risk limit: {blackjackPerfectAI.risk_factor}%\n')
        game_results.write(f'Player 2 (Only card counting): \n  Sets won: {sets_won_onlycount} \n  Set win percentage: {(sets_won_onlycount / sets) * 100} \n  Average payout: {average_onlycount / sets} \n  Best payout: {highest_amnt_onlycount} \n  Worst loss: {lowest_amnt_onlycount}\n')
        game_results.write(f'Player 3 (Only perfect strategy): \n  Sets won: {sets_won_onlydecisions} \n  Set win percentage: {(sets_won_onlydecisions / sets) * 100} \n  Average payout: {average_onlydecisions / sets} \n  Best payout: {highest_amnt_onlydecisions} \n  Worst loss: {lowest_amnt_onlydecisions}\n')
        game_results.write(f'Player 4 (No strategies used): \n  Sets won: {sets_won_simplebot} \n  Set win percentage: {(sets_won_simplebot / sets) * 100} \n  Average payout: {average_simplebot / sets} \n  Best payout: {highest_amnt_simplebot} \n  Worst loss: {lowest_amnt_simplebot}\n')
        game_results.write('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\------------------/////////////////////\n')
    
def reset_ai(): # function to reset the paramters of the ais
    #O(1) operations
    #Simply resetting all the integers from all the bots
    blackjackPerfectAI.cash = blackjackPerfectAI.starting_cash
    blackjackPerfectAI.betting_unit = 50
    blackjackPerfectAI.lowest_bet = 10
    blackjackPerfectAI.running_count = 0
    blackjackPerfectAI.true_count = 0
    
    blackjackOnlyCountAI.cash = blackjackOnlyCountAI.starting_cash
    blackjackOnlyCountAI.betting_unit = 50
    blackjackOnlyCountAI.lowest_bet = 10
    blackjackOnlyCountAI.running_count = 0
    blackjackOnlyCountAI.true_count = 0
    
    blackjackOnlyDecisionsAI.cash = blackjackOnlyDecisionsAI.starting_cash
    blackjackOnlyDecisionsAI.betting_unit = 50
    blackjackOnlyDecisionsAI.lowest_bet = 10
    
    simplebot.cash = simplebot.starting_cash
     
def startgame(): #starts a new game
    #Entire function consists of O(1) operations

    #creates new hands for all the players
    dealer_hand = []
    perfect_player_hand = []
    perfect_player_split_hand = []
    onlycount_bot_hand = []
    onlydecisions_bot_hand = []
    onlydecisions_bot_split_hand = []
    simplebot_hand = []
    
    # values to store bets
    perfect_player_bet = 0
    perfect_player_split_bet = 0
    onlycount_bot_bet = 0
    onlydecisions_bot_bet = 0
    onlydecisions_bot_split_bet = 0
    simplebot_bet = 0

    perfect_player_bet, onlycount_bot_bet, onlydecisions_bot_bet, simplebot_bet = new_round(dealer_hand, perfect_player_hand, onlycount_bot_hand, onlydecisions_bot_hand, simplebot_hand, perfect_player_bet, onlycount_bot_bet, onlydecisions_bot_bet, simplebot_bet) 
    # calls the new round function which returns all the bets, and passes in all the hands and bets as arguments
   
    #Getting the choice from the bots, passing the first card in the dealers hand, the bots hand, and the bots hand value as arguments
    if blackjackPerfectAI.make_choice(dealer_hand[0], perfect_player_hand, get_hand_val(perfect_player_hand)) == 'SP':
        #If the choice calls for a split
        perfect_player_split_hand = [perfect_player_hand[1]] # split the deck into two hands: The split deck consisting the of the second card
        perfect_player_hand = [perfect_player_hand[0]] #and the regular hand consisting only of the first card
        perfect_player_split_bet = perfect_player_bet #The split bet becomes the players bet 
        perfect_player_bet = make_choice(dealer_hand, blackjackPerfectAI.make_choice(dealer_hand[0], perfect_player_hand, get_hand_val(perfect_player_hand)), 
        perfect_player_hand, perfect_player_bet, True, blackjackPerfectAI) # The make_choice function is called for the hand containing the first card before the split, this will return when the algorithm decides it's time
                                                                           # to stop hitting
        perfect_player_split_bet = make_choice(dealer_hand, blackjackPerfectAI.make_choice(dealer_hand[0], perfect_player_split_hand, get_hand_val(perfect_player_split_hand)),  #The same thing is done for the split hand
        perfect_player_split_hand, perfect_player_split_bet, True, blackjackPerfectAI)
    else: #If the choice wasn't to split, then the player makes a regular move without splitting
        perfect_player_bet = make_choice(dealer_hand, blackjackPerfectAI.make_choice(dealer_hand[0], perfect_player_hand, get_hand_val(perfect_player_hand)), 
        perfect_player_hand, perfect_player_bet, False, blackjackPerfectAI)
        
    bot_hit(onlycount_bot_hand) # Hits for the bot that only counts card
    
    #Similar process to above but for the bot that only makes proper deicisions
    if blackjackOnlyDecisionsAI.make_choice(dealer_hand[0], onlydecisions_bot_hand, get_hand_val(onlydecisions_bot_hand)) == 'SP':
        onlydecisions_bot_split_hand = [onlydecisions_bot_hand[1]]
        onlydecisions_bot_hand = [onlydecisions_bot_hand[0]]
        onlydecisions_bot_split_bet = onlydecisions_bot_bet
        onlydecisions_bot_bet = make_choice(dealer_hand, blackjackOnlyDecisionsAI.make_choice(dealer_hand[0], onlydecisions_bot_hand, get_hand_val(onlydecisions_bot_hand)), 
        onlydecisions_bot_hand, onlydecisions_bot_bet, True, blackjackOnlyDecisionsAI)
        onlydecisions_bot_split_bet = make_choice(dealer_hand, blackjackOnlyDecisionsAI.make_choice(dealer_hand[0], onlydecisions_bot_split_hand, get_hand_val(onlydecisions_bot_split_hand)), 
        onlydecisions_bot_split_hand, onlydecisions_bot_split_bet, True, blackjackOnlyDecisionsAI)
    else:
        onlydecisions_bot_bet = make_choice(dealer_hand, blackjackOnlyDecisionsAI.make_choice(dealer_hand[0], onlydecisions_bot_hand, get_hand_val(onlydecisions_bot_hand)), 
        onlydecisions_bot_hand, onlydecisions_bot_bet, False, blackjackOnlyDecisionsAI)
        
    bot_hit(simplebot_hand) #The other bots hit
    bot_hit(dealer_hand)
    
    check_for_win(dealer_hand, perfect_player_hand, perfect_player_split_hand, onlycount_bot_hand, onlydecisions_bot_hand, onlydecisions_bot_split_hand, simplebot_hand, perfect_player_bet, perfect_player_split_bet, onlycount_bot_bet, onlydecisions_bot_bet, onlydecisions_bot_split_bet, simplebot_bet) # then checks for a win

def reshuffle(): # function to put all cards back in the deck
    #O(1)
    global full_deck
    # A single deck
    single_deck = ['AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC',
               'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
               'AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
               'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD']
    # A full deck consists of 8 single decks
    full_deck = single_deck * 8
    #Resets the running count of the AI's the count cards because
    #now all cards have returned to the deck so no advantage can be had
    blackjackPerfectAI.running_count = 0
    blackjackOnlyCountAI.running_count = 0

def new_round(dealer_hand, perfect_player_hand, onlycount_bot_hand, onlydecisions_bot_hand, simplebot_hand, perfect_player_bet, onlycount_bot_bet, onlydecisions_bot_bet, simplebot_bet): # function to clear all players hands and do the beginning actions of the game
    #O(1)
    global full_deck
    if len(full_deck) <= 40: # checks if the amount of cards remaining in the deck is less than or equal to 40
        reshuffle() # the decks gets reset 
    #Calls the make_bets function  that returns the bets for all the players
    perfect_player_bet, onlycount_bot_bet, onlydecisions_bot_bet, simplebot_bet = make_bets(perfect_player_bet, onlycount_bot_bet, onlydecisions_bot_bet, simplebot_bet)
    #Deals out cards to players
    deal(dealer_hand, perfect_player_hand, onlycount_bot_hand, onlydecisions_bot_hand, simplebot_hand) 
    organize_cards(perfect_player_hand) #The cards are organized so that a decision can easily be made to double down or split
    organize_cards(onlydecisions_bot_hand)
    return perfect_player_bet, onlycount_bot_bet, onlydecisions_bot_bet, simplebot_bet

def make_bets(perfect_player_bet, onlycount_bot_bet, onlydecisions_bot_bet, simplebot_bet): # function to make the bets for the players
    #O(1)
    # for the bot controlled players, the bet is based off what the bot decides
    perfect_player_bet = blackjackPerfectAI.make_bet_educated() 
    onlycount_bot_bet = blackjackOnlyCountAI.make_bet_educated()
    # the rest of the bots bet randomly, because it would be a shame to not let them in on the fun
    onlydecisions_bot_bet = random.randint(10,30)
    simplebot_bet = random.randint(10,30)
    return perfect_player_bet, onlycount_bot_bet, onlydecisions_bot_bet, simplebot_bet

def deal(dealer_hand, perfect_player_hand, onlycount_bot_hand, onlydecisions_bot_hand, simplebot_hand): # function to initially deal out cards to player and dealer
    global full_deck
    #O(1), for loop will always only ever deal out 2 cards
    for x in range(2): # deals out two cards to the players and dealer, then removes that card from the list
        dealer_hand.append(full_deck.pop(random.randint(0,len(full_deck) - 1)))
        perfect_player_hand.append(full_deck.pop(random.randint(0,len(full_deck) - 1)))
        onlycount_bot_hand.append(full_deck.pop(random.randint(0,len(full_deck) - 1)))
        onlydecisions_bot_hand.append(full_deck.pop(random.randint(0,len(full_deck) - 1)))
        simplebot_hand.append(full_deck.pop(random.randint(0,len(full_deck) - 1)))
        # calls the card counting method in blackjackPerfectAI, simulating how a card counter would count cards in real life
        if x == 0:
            # In blackjack, only the first card of the dealers' is face up, so that's the only one we count
            blackjackPerfectAI.count_new_card(dealer_hand[x], len(full_deck))
            blackjackOnlyCountAI.count_new_card(dealer_hand[x], len(full_deck))
        # otherwise, count every other card
        blackjackPerfectAI.count_new_card(perfect_player_hand[x], len(full_deck))
        blackjackPerfectAI.count_new_card(onlycount_bot_hand[x], len(full_deck))
        blackjackPerfectAI.count_new_card(onlydecisions_bot_hand[x], len(full_deck))
        blackjackPerfectAI.count_new_card(simplebot_hand[x], len(full_deck))
        
        blackjackOnlyCountAI.count_new_card(perfect_player_hand[x], len(full_deck))
        blackjackOnlyCountAI.count_new_card(onlycount_bot_hand[x], len(full_deck))
        blackjackOnlyCountAI.count_new_card(onlydecisions_bot_hand[x], len(full_deck))
        blackjackOnlyCountAI.count_new_card(simplebot_hand[x], len(full_deck))
        
def organize_cards(hand): # function that organizes the cards at the initial deal so that the highest card is always first
    # This is done so that the dictionaries on the bot side don't need to contain every possible combination of cards 
    # and can always be written with the ace as the first card. Doing this, the choices based on when the player has an ace and another card will be much easier
    # to determine
    #Always O(1)
    card1 = 0
    card2 = 0
    if hand[0][0] == '1' or hand[0][0] == 'J' or hand[0][0] == 'Q' or hand[0][0] == 'K':
        card1 = 10
    elif hand[0][0] == 'A':
        card1 = 11
    else:
        card1 = int(hand[0][0])
    # getting the value of the first card
    if hand[1][0] == '1' or hand[1][0] == 'J' or hand[1][0] == 'Q' or hand[1][0] == 'K':
        card2 = 10
    elif hand[1][0] == 'A':
        card2 = 11
    else:
        card2 = int(hand[1][0])
    # getting the value of the second card
    if card1 < card2: 
        # swap the values if the first card value is less than the second card value 
        hand[0], hand[1] = hand[1], hand[0]

def bot_hit(hand): # function that adds a new card to a players hand based on their current hand value
    #The worst-case time complexity of this function is O(n) where n is the amount of cards the hand needs before 
    #it's collective value equals or exceeds 17
    #The best-case time complexity is O(1), this occurs when the players hand initially is a value that equals or exceeds 17
    global full_deck # gets the full deck
    hand_val = 0 # gets the value of the players hand
    hand_val = get_hand_val(hand)
    if hand_val <= 17: # if the value of their hand is less than 17, another card is added to their hand
        new_card = full_deck.pop(random.randint(0,len(full_deck) - 1))
        hand.append(new_card)
        blackjackPerfectAI.count_new_card(new_card, len(full_deck))
        blackjackOnlyCountAI.count_new_card(new_card, len(full_deck))
        return bot_hit(hand) # this function is called again
    else: # otherwise, the function returns nothing
        return
        
def make_choice(dealer_hand, choice, hand, bet, split_check, currentAI): # function to perform the choice based on what was decided on the bot side
    #Worst-case time complexity of this function is O(n) where n is the amount of moves made before the bot chooses to stand
    #Best-case time complexity is O(1) when the bot chooses to double down
    global full_deck # gets the full deck
    choices = 0 # integer to store the amount of turns the player has performed
    while choice != 'S': # while the bot hasn't decided to stand
        if choice == 'H' or (choice == 'D' and choices >= 1) or (choice == 'SP' and split_check == True):
            # if the choice is to hit, or the choice is to double down but the bot has taken its first turn or to split but the player has already split
            # perform a regular hit
            new_card = full_deck.pop(random.randint(0,len(full_deck) - 1))
            hand.append(new_card)
            blackjackPerfectAI.count_new_card(new_card, len(full_deck))
            blackjackOnlyCountAI.count_new_card(new_card, len(full_deck))
            if get_hand_val(hand) >= 21:
                break
            else:
                choice = currentAI.make_choice(dealer_hand[0], hand, get_hand_val(hand))
        elif choice == 'D' and choices < 1:
            # if the choice is to double down, and the bot hasn't taken a turn yet
            # gets the card regularily then doubles the bet and breaks from the loop
            new_card = full_deck.pop(random.randint(0,len(full_deck) - 1))
            hand.append(new_card)
            blackjackPerfectAI.count_new_card(new_card, len(full_deck))
            blackjackOnlyCountAI.count_new_card(new_card, len(full_deck))
            bet *= 2
            break
        choices += 1
    return bet
                
def get_hand_val(hand): # function that returns the value of a players hand
    hand_val = 0 # stores the value of their hand
    has_ace = False # boolean to check if the player has an ace in their hand
    # this is needed because the value of the ace will change depending on the current value of the users hand
    ace_count = 0 # stores the amount of aces someone has
    #Loop runs for O(n) where n is the size of the hand
    for card in hand: # for every card in their hand
        card_val = card[0] # gets the first character of the card, this can determine every card in the deck
        if card_val == 'A': # if the card is an ace
            has_ace = True # set has_ace to true and increase the ace_count
            ace_count += 1
        elif card_val == '1' or card_val == 'J' or card_val == 'Q' or card_val == 'K':
            # if the first character is a 1 (10), J(ack), (Q)ueen, or (K)ing, increase the hand count by 10
            hand_val += 10
        else: # otherwise just add in the integer value of the first one digit character
            hand_val += int(card_val)
    if has_ace: # if the player had an ace
        for x in range(ace_count): # for every ace that they have
            if hand_val <= 10: # if their hand value is less than 10, make that ace count for eleven
                hand_val += 11
            else: #otherwise make it count for 1
                hand_val += 1
    return hand_val

def check_for_win(dealer_hand, perfect_player_hand, perfect_player_split_hand, onlycount_bot_hand, onlydecisions_bot_hand, onlydecisions_bot_split_hand, simplebot_hand, perfect_player_bet, perfect_player_split_bet, onlycount_bot_bet, onlydecisions_bot_bet, onlydecisions_bot_split_bet, simplebot_bet): # function that checks who won the game
    #Time complexity for this function is O(n) where n is the amount of bets that are in play (ranges from 4-6)
    players_won = 0 # keeps track of numbers of players that won, tied and got a blackjack
    players_tied = 0
    players_blackjack = 0
    player_hand_counts = [] # list to hold player hand value counts
    player_hands = []
    busted = [] # list to hold players who busted
    initial_bets = [] #List to hold the bets
    resulting_bets = [] #List to hold bets after a decision has been made on them 
    
    # getting the value of everyones hands
    val_to_beat = get_hand_val(dealer_hand) 
    blackjackPerfectAI.count_new_card(dealer_hand[1], len(full_deck)) #counting the dealers second card because now it's been revealed
    blackjackOnlyCountAI.count_new_card(dealer_hand[1], len(full_deck))
    
    player_hands.append(perfect_player_hand)
    player_hand_counts.append(get_hand_val(perfect_player_hand)) # puts all the player hands in the list
    initial_bets.append(perfect_player_bet)
    resulting_bets.append(perfect_player_bet)
    
    if len(perfect_player_split_hand) > 0:
        # if the len of the split hand is greater than 0, then the bot has split, and the hand value is considered
        player_hands.append(perfect_player_split_hand)
        player_hand_counts.append(get_hand_val(perfect_player_split_hand))
        initial_bets.append(perfect_player_split_bet)
        resulting_bets.append(perfect_player_split_bet)
    
    player_hands.append(onlycount_bot_hand)
    player_hand_counts.append(get_hand_val(onlycount_bot_hand))
    initial_bets.append(onlycount_bot_bet)
    resulting_bets.append(onlycount_bot_bet)
    
    player_hands.append(onlydecisions_bot_hand)
    player_hand_counts.append(get_hand_val(onlydecisions_bot_hand))
    initial_bets.append(onlydecisions_bot_bet)
    resulting_bets.append(onlydecisions_bot_bet)
    
    #similar for the only decisions bot
    if len(onlydecisions_bot_split_hand) > 0:
        player_hands.append(onlydecisions_bot_split_hand)
        player_hand_counts.append(get_hand_val(onlydecisions_bot_hand))
        initial_bets.append(onlydecisions_bot_split_bet)
        resulting_bets.append(onlydecisions_bot_split_bet)
    
    player_hands.append(simplebot_hand)
    player_hand_counts.append(get_hand_val(simplebot_hand))
    initial_bets.append(simplebot_bet)
    resulting_bets.append(simplebot_bet)
    
    print(val_to_beat, player_hand_counts)
    
    for hand in range(len(player_hands)):
        if player_hands[hand][0][0] == 'A' and (player_hands[hand][1][0] == '1' or player_hands[hand][1][0] == 'J' or player_hands[hand][1][0] == 'Q' or player_hands[hand][1][0] == 'K'):
            players_blackjack += 1
            resulting_bets[hand] *= 1.5
            if players_won > 1: 
                print(', ', end = "")
            print(f'Hand {hand + 1} ', end = "")
    if players_blackjack > 1: # different statements depending on how many players won 
        print('have gotten a blackjack and won 2.5x their bet!')
    elif players_blackjack == 1:
        print('has gotten a blackjack and won 2.5x their bet!')
    else:
        print('No one got a blackjack!') 
    
    #O(n) operation
    for x in range(len(player_hand_counts)): # for every count in the list
        if player_hand_counts[x] > 21: # if the players hands was greater than 21, meaning they busted
            busted.append(True) # sets their index in the busted list to True
            resulting_bets[x] *= -1
        else: # otherwise sets it to False
            busted.append(False)
   
    if val_to_beat > 21: # if the dealer busts 
        print('The dealer busted and everyone who hasn\'t busted won their bets!')

    else: # if the dealer didn't bust
        #O(n) operation
        for x in range(len(player_hand_counts)): # for each player count, checks if the player beat the dealer and didnt bust
            if player_hand_counts[x] > val_to_beat and busted[x] == False:
                players_won += 1 # adds 1 to the count of players that won
                if players_won > 1: # if the amount of players that won is greater than 1, a comma is printed to make everything look nice
                    print(', ', end = "")
                print(f'Hand {x + 1} ', end = "") # adds that their hand won to a string
            elif player_hand_counts[x] < val_to_beat and busted[x] == False: # if the player didn't win
                resulting_bets[x] *= -1 # takes away their bet 
        if players_won > 1: # different statements depending on how many players won 
            print('have beat the dealer and won twice their bet!')
        elif players_won == 1:
            print('has beat the dealer and won twice their bet!')
        else:
            print('No one beat the dealer!') 
            
        #O(n) operation
        for x in range(len(player_hand_counts)): # similar to above but now checking for ties
            if player_hand_counts[x] == val_to_beat:
                players_tied += 1
                resulting_bets[x] = 0
                if players_tied > 1:
                    print(', ', end = "")
                print(f'Hand {x + 1} ', end = "")
        if players_tied > 1:
            print('have tied with the dealer and won their bet back!')
        elif players_tied == 1:
            print('has tied with the dealer and won their bet back!')
        else:
            print('No one tied with the dealer!')
             

    
    
    #Because only the PerfectAI and the OnlyDecisionsAI are counting cards and betting based on that,
    #previous card_count result history will only be recorded for their outcomes.
    #This is why this list is being used
    info_to_record = []
    
    blackjackPerfectAI.cash += resulting_bets[0]
    info_to_record.append((initial_bets[0], resulting_bets[0]))
    #A tuple is appended whenever a bot using card counting receives their bet
    #The tuple consists of their initial bet and their resulting bet
    
    #At this point, all the bets have been counted, now they must be added to their respective cash amounts
    #3 scenarios exist because of how the game is set up, which changes which bets in the list belong to who.
    #In the first scenario, the perfect_player bot has split bot the onlydecisions_bot hasn't so the respective cash values are added
    #In the second scenario, the perfect_player bot hasn't split bot the onlydecisions_bot has
    #In the thirs scenario, both players have split
    #In the last scenario, neither of the bots have split
    if len(perfect_player_split_hand) > 0 and len(onlydecisions_bot_split_hand) == 0:
        blackjackPerfectAI.cash += resulting_bets[1]
        blackjackOnlyCountAI.cash += resulting_bets[2]  
        blackjackOnlyDecisionsAI.cash += resulting_bets[3]
        simplebot.cash += resulting_bets[4]
        
        info_to_record.append((initial_bets[1], resulting_bets[1]))
        info_to_record.append((initial_bets[3], resulting_bets[3]))
        
    elif len(perfect_player_split_hand) == 0 and len(onlydecisions_bot_split_hand) > 0:
        blackjackOnlyCountAI.cash += resulting_bets[1]
        blackjackOnlyDecisionsAI.cash += resulting_bets[2]
        blackjackOnlyDecisionsAI.cash += resulting_bets[3]
        simplebot.cash += resulting_bets[4]
        
        info_to_record.append((initial_bets[2], resulting_bets[2]))
        info_to_record.append((initial_bets[3], resulting_bets[3]))
        
    elif len(perfect_player_split_hand) > 0 and len(onlydecisions_bot_split_hand) > 0:
        blackjackPerfectAI.cash += resulting_bets[1]
        blackjackOnlyCountAI.cash += resulting_bets[2]
        blackjackOnlyDecisionsAI.cash += resulting_bets[3]
        blackjackOnlyDecisionsAI.cash += resulting_bets[4]
        simplebot.cash += resulting_bets[5]
        
        info_to_record.append((initial_bets[1], resulting_bets[1]))
        info_to_record.append((initial_bets[3], resulting_bets[3]))
        info_to_record.append((initial_bets[4], resulting_bets[4]))
        
    elif len(perfect_player_split_hand) == 0 and len(onlydecisions_bot_split_hand) == 0:
        blackjackOnlyCountAI.cash += resulting_bets[1]
        blackjackOnlyDecisionsAI.cash += resulting_bets[2]
        simplebot.cash += resulting_bets[3]
        
        info_to_record.append((initial_bets[2], resulting_bets[2]))
    
    #If the true count is greater than or equal to 1, then record the results
    if blackjackPerfectAI.true_count >= 1:
        collect_data(blackjackPerfectAI.true_count, blackjackPerfectAI.risk_factor, info_to_record)
    
    print(initial_bets)
    print(resulting_bets)
    
def collect_data(card_count, risk_factor, betting_info):
    #O(n) operation where n is the amount of tuples in betting_info
    if os.path.isdir(f'previous_bet_results/{risk_factor}') == False:
        #Checks if the folder exists, if not, create the folder
        os.mkdir(f'previous_bet_results/{risk_factor}')
    with open(f'previous_bet_results/{risk_factor}/{card_count}.txt', 'a+') as data_file:
        #Creates (if needed) and opens the file of the corresponding card count, then appends
        #the data
        for bet in betting_info:
            if bet[1] == bet[0]:
                data_file.write('W\n')
            elif bet[1] == 0:
                data_file.write('T\n')
            elif bet[1] < 0:
                data_file.write('L\n') 


initgame()






