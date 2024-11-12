import random, time

BALANCE = 2000
BLIND_AMOUNT = 100

WIN_MULTIPLIER = 3

user_wins = 0
user_losts = 0
user_ties = 0
total_rounds = 0

bluff_lines = [
    "I've got a full house ready!",
    "You won't believe my hand!",
    "I've seen better cards in my sleep.",
    "All bets are off!",
    "I'm playing my ace in the hole.",
    "My hand is unbeatable!",
    "Don't underestimate my luck!",
    "I've got my eyes on the prize.",
    "You're about to lose this round.",
    "I smell victory in the air.",
    "I hold the winning card!",
    "You should be sweating right now.",
    "This hand is my secret weapon.",
    "I've got a straight flush up my sleeve.",
    "Your chances just got slimmer!",
    "It's game over for you!"
]

draw_cards_explained = {
    "drawing cards": "comma-separated (1, 3) or 'none' to keep",
    "minimum": 1,
    "maximum": 5
}

def deal_cards():
    deck = [f"{rank}{suit}" for rank in '23456789tJQKA' for suit in '♠♥♦♣']
    random.shuffle(deck)
    return deck[:5], deck[5:10]

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
            print("Please enter a valid number.")

def go_all_in():
    global BALANCE, bet_amount

    bet_amount = BALANCE
    BALANCE -= bet_amount
    print(f"You went all in (${bet_amount})!")

def draw_single_card(deck):
    return deck.pop()

def draw_cards(hand, deck):
    global BLIND_AMOUNT, bet_amount
    bet_amount = BLIND_AMOUNT
    print()
    
    for key, value in draw_cards_explained.items():
        print(f"{key.title()}: {value}")

    print(f"\nYour current hand: {hand}")
    time.sleep(1)

    while True:
        to_draw = input("\nWhat would you like to do? ")
        if to_draw.lower() == 'none':
            break
        try:
            indices = [int(x) - 1 for x in to_draw.split(',')]
            for index in indices:
                if 0 <= index < len(hand):
                    hand[index] = draw_single_card(deck)
            print(f"Your new hand: {hand}")
            break
        except ValueError:
            print("Invalid input. Please try again.")

def get_fold():
    global BALANCE, bet_amount, user_losts, BLIND_AMOUNT

    bet_amount = BLIND_AMOUNT

    print(f"You folded. You lost your bet of: ${bet_amount}.")
    BALANCE -= bet_amount
    user_losts += 1
    time.sleep(1.25)

def bot_phrase():
    return random.choice(bluff_lines)

def get_deciding(player_hand, bot_hand):
    global BALANCE, WIN_MULTIPLIER, bet_amount, user_wins, user_losts, user_ties, action

    player_score = evaluate_hand(player_hand)
    bot_score = evaluate_hand(bot_hand)

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

def evaluate_hand(hand):
    score = sum(['23456789tJQKA'.index(card[0]) + 1 for card in hand])
    return score

# Main code:
def main():
    global total_rounds

    print("Welcome to Cantredraw!")
    time.sleep(1)

    while BALANCE > 0:
        total_rounds += 1

        print(f"\nRound {total_rounds}: You have ${BALANCE}.")
        print("\nDealing cards...")

        player_hand, bot_hand = deal_cards()
        deck = [f"{rank}{suit}" for rank in '23456789tJQKA' for suit in '♠♥♦♣']
        random.shuffle(deck)
        print(f"Your hand: {player_hand}")

        time.sleep(2)
        get_blinds()

        action = input("\nDo you want to (c)all, (b)et, go (a)ll in, (d)raw cards, or (f)old? ").lower()
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
            print()
            continue

        elif action in ["all in", "a"]:
            go_all_in()

        elif action in ["draw cards", "d"]:
            draw_cards(player_hand, deck)

        else:
            print("Invalid action.")
            continue

        time.sleep(1)
        print(f"\nBot's hand: {bot_hand}")
        print(f"Bot says: {bot_phrase()}")

        print("Deciding...")
        time.sleep(5)
        get_deciding(player_hand, bot_hand)
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

    print("\n* C Stats *")
    print(f"You left with: ${BALANCE}.")
    print(f"You won: {user_wins} times.")
    print(f"You lost: {user_losts} times.")
    print(f"You tied: {user_ties} times.")
    print(f"Total rounds played: {total_rounds}.")


# main()
