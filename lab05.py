########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
# 1. Mohamed Elgasim
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        play = input('Play again?\n')
        if play == 'Y' or 'Yes':
            return get_bank()
        elif play == 'N' or 'No':
            return play
        else:
            print('Please enter another value')
            return play
    return True
    
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    bank = int(input('How many chips do you want to start with?\n'))
    if bank >= 101: # checks to see if the user input for bank is greater than 100 or less than 0 and keeps asking if it is
        print('Too high a value, you can only choose 1-100 chips')
        bank = int(input('How many chips do you want to start with?\n'))
    elif bank <= 0:
        print('Too low a value, you can only choose 1-100 chips')
        bank = int(input('How many chips do you want to start with?\n'))
    else:
        wager = int(input('How many chips do you want to wage?'))
        if wager > bank:
            print('The wager amount cannot be greater than how much you have.', wager)
            wager = int(input('How many chips do you want to wage?'))
        if wager < 0: 
            print('The wager amount must be greater than 0.  Please enter again.')
            wager = int(input('How many chips do you want to wage?'))
        return wager

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    # assigns the three user random integers reels (a,b,c) between 1 and 10 
    reela = random.randint(1,10)
    reelb = random.randint(1,10)
    reelc = random.randint(1,10)
    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    matches = 0
    if reela == reelb: #checks which reel is equal to which and adds the matches accordingly and if none is equal, mathches are 0. Then return the number of matches 
        matches +=2
        if reela == reelc:
            matches += 1
    elif reela == reelc:
        matches += 2
        if reela == reelb:
            matches += 1
    elif reelb == reelc:
        matches += 2
        if reelb == reelc:
            matches += 1
    else:
        matches = 0
    return matches

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    num = 0
    while num == 0: #asks the user for the number of their chips and assigns it to bankstart if the num is equal to 0
        bankstart = int(input('How many chips do you want to start with?\n'))
        if bankstart <= 0:
            print('Too low of a value, you can only choose between 1 - 100 chips')
        elif bankstart > 100:
            print('Too high a value, you can only choose between 1 - 100 chips')
        else:
            num = 1
    return bankstart
    return 0

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3: #assigns the x value by multiplying it based on the number of matches won 
        x = (wager * 10) - wager
    elif matches == 2:
        x = (wager * 3) - wager
    elif matches == 0:
        x = wager - wager - wager
    return x

if __name__ == "__main__":
    playing = True
    while playing:
        bank = get_bank
        while True:  # Replace with condition for if they still have money.
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
