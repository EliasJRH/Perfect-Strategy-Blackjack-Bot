
starting_cash = 1000
cash = starting_cash
betting_unit = 20
lowest_bet = 10
running_count = 0
true_count = 0
    
    
# Dictionary to store what each card contributes to the running count in a game
# 10 - A: -1, 2-6: 1, 7-9: 0
# While taking up slightly more memory and space, the program is able to retrieve
# card counts faster then if a check was ran on each card everytime    
card_count_vals = {
    'A' : -1,
    '2' : 1,
    '3' : 1,
    '4' : 1,
    '5' : 1,
    '6' : 1,
    '7' : 0,
    '8' : 0,
    '9' : 0,
    '1' : -1,
    'J' : -1,
    'Q' : -1,
    'K' : -1
}    
    
def count_new_card(new_card, cards_remaining): # function to change the running count and true count based on what cards have been dealt
    global running_count # gets the global values for running and true count
    global true_count
    running_count += card_count_vals[new_card[0]] # the true count changes based off the card counting value of the card that was just dealt
    true_count = int((running_count / (round((cards_remaining / 52) * 2) / 2))) # True count is calculated
    # Formula for true count is (running count / # of decks remaining to nearest half)
    # The true count is what is used to make bets 
   
def make_bet_educated(): # function to calculate how much should be bet
    if true_count < 1: # if the true count is less than 1, the bot bets the lowest amount that it can
        return lowest_bet
    return betting_unit * true_count # otherwise, it bets betting unit x true count 