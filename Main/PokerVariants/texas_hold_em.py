import random, time

BALANCE = 2000
BLIND_AMOUNT = 100

WIN_MULTIPLIER = 2

user_wins = 0
user_losts = 0
user_ties = 0
total_rounds = 0

bluff_lines = [
    "I have a strong hand.",
    "You should've folded.",
    "I'm all in!",
    "I don't think you can beat me.",
    "I've got a royal flush.",
    "You won't win this one.",
    "I'm feeling lucky.",
    "I have two pairs.",
    "You should be scared.",
    "I know what I'm doing.",
    "I can read you like a book.",
    "This is my game.",
    "You can't bluff a bluffer.",
    "I'm not worried at all.",
    "I have the winning hand.",
    "A high card is more than enough.", # from here down, I added my own bluff lines :D
    "You don't even have one pair!",
    "Full house is the best!",
    "Three of a kind is not so kind.",
    "I got a straight.",
    "I love flusher, flushy, flush, flush!"
]

def deal_cards():
    deck = [f"{rank}{suit}" for rank in '23456789tJQKA' for suit in '♠♥♦♣']
    random.shuffle(deck)
    return deck[:2], deck[2:4]
    
def get_blinds():
    global BALANCE, BLIND_AMOUNT, bot_bet

    BALANCE -= BLIND_AMOUNT
    print(f"\nYou posted a Small Blind of: ${BLIND_AMOUNT}. Remaining money: ${BALANCE}.")
    
    bot_bet = BLIND_AMOUNT * 2
    print(f"Bot posted a Big Blind of: ${bot_bet}.")


def get_call():
    global bet_amount, bot_bet, BALANCE

    bet_amount = bot_bet 
    
    BALANCE -= bet_amount
    print(f"You called ${bet_amount}. Remaining money: ${BALANCE}.")

def get_bet():
    global BALANCE, bet_amount

    while True:
        bet_amount = input("How much do you want to bet? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if 1 <= bet_amount <= BALANCE:
                break
            else:
                print(f"Amount must be between: $1 - ${BALANCE}")
        else:
            print("Please enter a number next time.")

def go_all_in():
    global BALANCE, bet_amount

    bet_amount = BALANCE
    BALANCE -= bet_amount
    print(f"You went all in (${bet_amount})!")

def get_fold():
    global BALANCE, BLIND_AMOUNT, bet_amount, user_losts

    bet_amount = BLIND_AMOUNT

    print(f"You folded. You lost your bet of: ${bet_amount}.")
    BALANCE -= bet_amount
    user_losts += 1
    time.sleep(1.25)


def bot_phrase():
    return random.choice(bluff_lines)

def get_deciding():
    global BALANCE, bet_amount, player_score, bot_score, user_wins, user_losts, user_ties, WIN_MULTIPLIER

    player_score = random.randint(1, 10)
    bot_score = random.randint(1, 10)
        
    if player_score > bot_score:
        print(f"You win! Your score: {player_score}, Bot's score: {bot_score}.")
        BALANCE += bet_amount * 2
        user_wins += 1 * WIN_MULTIPLIER

    elif player_score == bot_score:
        print(f"It's a tie! Your score: {player_score}, Bot's score: {bot_score}.")
        BALANCE += bet_amount
        user_ties += 1

    else:
        print(f"You lost! Your score: {player_score}, Bot's score: {bot_score}.")
        BALANCE -= bet_amount
        user_losts += 1


# Main code:
def main():
    global total_rounds

    print("Welcome to Texas Hold Em'!")
    time.sleep(1)

    while BALANCE > 0:
        total_rounds += 1

        print(f"\nRound {total_rounds}: You have ${BALANCE}.")
        print("\nDealing cards...")

        player_hand, bot_hand = deal_cards()
        print(f"Your hand: {player_hand}")

        time.sleep(2)
        get_blinds()

        action = input("\nDo you want to (c)all, (b)et, go (a)ll in, or (f)old? ").lower()
        if action in ["bet", "b"]:
            get_bet()
            
        elif action in ["call", "c"]:
            bet_amount = bot_bet
            if bet_amount > BALANCE:
                print("You don't have enough money to call.")
                continue
            else:
                get_call()

        elif action in ["fold", "f"]:
            get_fold()
            continue
            
        elif action in ["all in", "a"]:
            go_all_in()
            
        else:
            print("Invalid action.")
            continue

        time.sleep(1)
        print(f"\nBot's hand: {bot_hand}")
        print(f"Bot says: {bot_phrase()}")

        print("Deciding...")
        time.sleep(5)
        get_deciding()
        time.sleep(1.25)
        print()

        while True:
            answer = input("Enter 'Y' to play again (Q to quit): ")
            if answer.upper() == "Q":
                break
            elif answer.upper() == "Y":
                break
            else:
                print("Invalid answer.")

        if answer.upper() == "Q":
            break

    print("\n* THE Stats *")
    print(f"You left with: ${BALANCE}.")
    print(f"You won: {user_wins} times.")
    print(f"You lost: {user_losts} times.")
    print(f"You tied: {user_ties} times.")
    print(f"The total rounds played: {total_rounds}.")
    time.sleep(2)


# main()
